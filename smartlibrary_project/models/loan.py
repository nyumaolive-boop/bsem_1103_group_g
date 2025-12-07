from datetime import date, timedelta

class Loan:
    def __init__(self, id_, book_id, member_id, loan_date, due_date,
                 return_date, status):
        self.id = id_
        self.book_id = book_id
        self.member_id = member_id
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = return_date
        self.status = status

    @staticmethod
    def default_due_date(loan_date=None):
        """
        Calculate the default due date for a loan.

        If no loan_date is provided, use today's date.
        Then add 7 days to get the due date.

        Returns:
            a datetime object representing the due date.
        """
        if loan_date is None:
            loan_date = date.today()
        return loan_date + timedelta(days=7)
