from db import get_connection

class DashboardService:
    def get_summary(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                # total number of books in a library
                cur.execute("SELECT COUNT(*) AS total_books FROM books;")
                total_books = cur.fetchone()["total_books"]

                #total number of registered library members
                cur.execute("SELECT COUNT(*) AS total_members FROM members;")
                total_members = cur.fetchone()["total_members"]

                #how many loans are currently active (not yet returned)
                cur.execute("SELECT COUNT(*) AS active_loans FROM loans WHERE status = 'ACTIVE';")
                active_loans = cur.fetchone()["active_loans"]

                # how many loans are currently overdue (not returned, past due date)
                cur.execute("SELECT COUNT(*) AS overdue_loans FROM loans WHERE status = 'OVERDUE';")
                overdue_loans = cur.fetchone()["overdue_loans"]

                # top 5 most borrowed books (by count of loans)
                cur.execute(
                    """
                    SELECT b.title, COUNT(*) AS times_borrowed
                    FROM loans l
                    JOIN books b ON b.id = l.book_id
                    GROUP BY b.title
                    ORDER BY times_borrowed DESC
                    LIMIT 5;
                    """
                )
                top_books = cur.fetchall()

        # send everything back as one dictionary for the UI to display
        return {
            "total_books": total_books,
            "total_members": total_members,
            "active_loans": active_loans,
            "overdue_loans": overdue_loans,
            "top_books": top_books,
        }
