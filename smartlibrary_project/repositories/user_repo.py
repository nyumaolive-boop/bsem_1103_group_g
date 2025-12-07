from db import get_connection
import hashlib

class UserRepository:
    def find_by_username(self, username):
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT u.id, u.username, u.full_name,
                           r.name AS role_name, u.password_hash
                    FROM users u
                    JOIN roles r ON r.id = u.role_id
                    WHERE u.username = %s AND u.is_active = TRUE
                    """,
                    (username,),
                )
                row = cur.fetchone()
        return row

    def hash_password(self, plain_password):
        return hashlib.sha256(plain_password.encode("utf-8")).hexdigest()

    def verify_password(self, stored_hash, plain_password):
        return stored_hash == self.hash_password(plain_password)
