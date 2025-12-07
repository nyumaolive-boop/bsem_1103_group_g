class Book:
    def __init__(self, id_, title, isbn, category, published_year,
                 total_copies, available_copies):
        self.id = id_
        self.title = title
        self.isbn = isbn
        self.category = category
        self.published_year = published_year
        self.total_copies = total_copies
        self.available_copies = available_copies

    def is_available(self):
        """
        Return True if at least one copy is available to borrow,
        otherwise return False.
        """
        return self.available_copies > 0
