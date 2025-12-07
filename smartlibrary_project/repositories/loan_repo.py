from db import get_connection

class LoanRepository:
    def count_active_loans(self, member_id, conn=None):
        external_conn = conn is not None
        if not external_conn:
            conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT COUNT(*) AS cnt
                FROM loans
                WHERE member_id = %s AND status = 'ACTIVE'
                """,
                (member_id,),
            )
            row = cur.fetchone()
        if not external_conn:
            conn.close()
        return row["cnt"]

    def get_loan(self, loan_id, conn=None):
        external_conn = conn is not None
        if not external_conn:
            conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT * FROM loans WHERE id = %s
                """,
                (loan_id,),
            )
            row = cur.fetchone()
        if not external_conn:
            conn.close()
        return row
