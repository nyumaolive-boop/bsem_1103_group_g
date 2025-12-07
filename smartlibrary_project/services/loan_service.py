from datetime import date, timedelta
from db import get_connection
from repositories.loan_repo import LoanRepository

# business rules / constants
MAX_ACTIVE_LOANS = 3   # e.g. each member can only have 3 active loans
LOAN_DAYS = 7          # each loan lasts for 7days

class LoanService:
    def __init__(self):
        # repository that knows how to query loans table
        self.loan_repo = LoanRepository()

    def create_loan(self, book_id, member_id):
        """
        creates a new loan for a member.

        steps:
        1. check how many active loans the member already has.
        2. check if the book has available copies.
        3. insert a new row into the loans table.
        4. decrease the available_copies of the book.
        5. return the ID of the new loan.
        """
        with get_connection() as conn:
            with conn.cursor() as cur:
                # 1. count existing active loans for this member
                active = self.loan_repo.count_active_loans(member_id, conn)
                if active >= MAX_ACTIVE_LOANS:
                    # business rule: limit active loans
                    raise ValueError("Member already has 3 active loans.")

                # 2. check if the selected book is available
                cur.execute(
                    "SELECT available_copies FROM books WHERE id = %s;",
                    (book_id,),
                )
                row = cur.fetchone()
                if not row or row["available_copies"] <= 0:
                    raise ValueError("Book not available.")

                # 3. calculate loan_date and due_date
                loan_date = date.today()
                due_date = loan_date + timedelta(days=LOAN_DAYS)

                # 4. insert the new loan and get its generated ID
                cur.execute(
                    """
                    INSERT INTO loans (book_id, member_id, loan_date, due_date, status)
                    VALUES (%s, %s, %s, %s, 'ACTIVE')
                    RETURNING id;
                    """,
                    (book_id, member_id, loan_date, due_date),
                )
                loan_id = cur.fetchone()["id"]

                # 5. decrease available copies for the book
                cur.execute(
                    "UPDATE books SET available_copies = available_copies - 1 WHERE id = %s;",
                    (book_id,),
                )

        # the context manager will commit and close connection
        return loan_id

    def return_loan(self, loan_id):
        """
        process the return of a loaned book.
        steps:
        1. fetch the loan by ID  and ensure it is active.
        2. decide new status:
            - RETURNED if on or before due date
            - OVERDUE_RETURNED if after due date
        3. update the loan's return_date and status.
        4. increase the book's available_copies again.
        """

        with get_connection() as conn:
            with conn.cursor() as cur:
                # 1. get the loan row (using repository, with same connection)
                loan = self.loan_repo.get_loan(loan_id, conn)
                if not loan or loan["status"] != "ACTIVE":
                    raise ValueError("Loan not active.")

                # 2. determine the new status based on today's date
                today = date.today()
                new_status = "RETURNED"
                if today > loan["due_date"]:
                    new_status = "OVERDUE_RETURNED"

                    # 3. update the loan record
                cur.execute(
                    """
                    UPDATE loans
                    SET return_date = %s, status = %s
                    WHERE id = %s;
                    """ ,
                    (today, new_status, loan_id),
                )

                # 4. increase available copies for the book
                cur.execute(
                    "UPDATE books SET available_copies = available_copies + 1 WHERE id = %s;",
                    (loan["book_id"],),
                )
