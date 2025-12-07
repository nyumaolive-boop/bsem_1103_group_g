from .user import User
from .book import Book
from .loan import Loan
from .bookclub import BookClub

# when someone writes: from models import *
# only these names will be imported.
__all__ = ["User", "Book", "Loan", "BookClub"]
