from repositories.user_repo import UserRepository
from models.user import User

class AuthService:
    def __init__(self):
        # Create an instance of the repository that talks to the DB
        self.user_repo = UserRepository()

    def login(self, username, password):
        """
        Try to log user.

        steps:
        1. look up the user by username.
        2. if no user is found, return None.
        3. if the password is wrong, return None.
        4. if everything is correct, return User object.
        """

        # 1. get the database row for this username
        row = self.user_repo.find_by_username(username)

        # 2. no such user is the database
        if not row:
            return None

        # 3. password does not match (hash comparison)
        if not self.user_repo.verify_password(row["password_hash"], password):
            return None

        # 4. login success, build a user model from the row
        return User(
            id_=row["id"],
            username=row["username"],
            full_name=row["full_name"],
            role_name=row["role_name"],
        )
