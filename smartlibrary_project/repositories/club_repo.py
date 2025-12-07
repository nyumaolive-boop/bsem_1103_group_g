from db import get_connection

class ClubRepository:
    def list_clubs(self):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT id, name, description, meeting_day, is_active FROM book_clubs ORDER BY name;"
                )
                return cur.fetchall()
