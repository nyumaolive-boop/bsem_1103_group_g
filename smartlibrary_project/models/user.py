class User:
    def __init__(self, id_, username, full_name, role_name):
        self.id = id_
        self.username = username
        self.full_name = full_name
        self.role_name = role_name

    @property
    def is_librarian(self):
        """
        True if this user is a member of librarian.
        compares role_name in a case-insensitive way.
        """
        return self.role_name.upper() == "LIBRARIAN"

    @property
    def is_member(self):
        """
        True if this user is a normal member ( not librarian ).
        """
        return self.role_name.upper() == "MEMBER"
