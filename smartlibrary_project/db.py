import psycopg2
from psycopg2.extras import RealDictCursor
import os

def get_connection():
    """
    Establishes and returns a PostgreSQL database connection.

    Environment variables are used if available, making the app flexible
    when developed on different machines. If environment variables are missing,
    default values (the second argument)are used.

    RealDictCursor ensures that query results are returned as dictionaries,
    e.g., row["username"], which is easier to work with than tuples.
    """
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "smartlibrary"),   # Database name
        user=os.getenv("DB_USER", "postgres"),         # DB username
        password=os.getenv("DB_PASSWORD", "Joma1234"), # Database password (default)
        host=os.getenv("DB_HOST", "localhost"),        # Database server location
        port=os.getenv("DB_PORT", "5432"),             # PostgreSQL default port
        cursor_factory=RealDictCursor                  # Return rows as dicts
    )
