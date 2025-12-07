from db import get_connection
from models.book import Book

class BookRepository:
    def get_all(self, search_term=None):
        query = """
            SELECT * FROM books
            WHERE (%s IS NULL OR LOWER(title) LIKE LOWER('%%' || %s || '%%'))
            ORDER BY title;
        """

        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, (search_term, search_term))
                rows = cur.fetchall()
# Convert database rows Books objects
        return [
            Book(
                id_=r["id"],
                title=r["title"],
                isbn=r["isbn"],
                category=r["category"],
                published_year=r["published_year"],
                total_copies=r["total_copies"],
                available_copies=r["available_copies"],
            )
            for r in rows
        ]
