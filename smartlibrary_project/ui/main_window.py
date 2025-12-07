from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QTabWidget, QTableWidget, QTableWidgetItem,
    QPushButton, QHBoxLayout, QLineEdit
)
from repositories.book_repo import BookRepository
from services.dashboard_service import DashboardService

# mianWindow is the central window after successful login
class MainWindow(QMainWindow):
    def __init__(self, user):
        super().__init__()

        # user information passed from login
        self.user = user

        # repository and services used by the UI
        self.book_repo = BookRepository()
        self.dashboard_service = DashboardService()

        # dynamic window title showing the logging-in user
        self.setWindowTitle(f"SmartLibrary - {self.user.full_name} ({self.user.role_name})")

        # build the UI tabs and layout
        self._build_ui()

    def _build_ui(self):
        # tab widget that holds multiple sections of the system
        tabs = QTabWidget()

        # add each feature as a separate tab
        tabs.addTab(self._build_catalog_tab(), "Book Catalog")
        tabs.addTab(self._build_loans_tab(), "Loans")
        tabs.addTab(self._build_clubs_tab(), "Book Clubs")
        tabs.addTab(self._build_dashboard_tab(), "Dashboard")

        # create a container to place the tabs inside the main window
        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        container.setLayout(layout)

        #set container as the central UI element of the window
        self.setCentralWidget(container)

        # default window size
        self.resize(900, 600)

    # --- Catalog Tab ---
    # creates the book catalog UI tab
    def _build_catalog_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # search bar for filtering books by title
        search_layout = QHBoxLayout()
        self.catalog_search = QLineEdit()
        self.catalog_search.setPlaceholderText("Search by title...")

        # search button triggers book loading
        btn_search = QPushButton("Search")
        btn_search.clicked.connect(self.load_books)

        # add search input and button to search layout
        search_layout.addWidget(self.catalog_search)
        search_layout.addWidget(btn_search)

        # table where books will be displayed
        self.catalog_table = QTableWidget(0, 5)
        self.catalog_table.setHorizontalHeaderLabels(
            ["ID", "Title", "Category", "Year", "Available"]
        )

        # add search row and table to the page layout
        layout.addLayout(search_layout)
        layout.addWidget(self.catalog_table)
        widget.setLayout(layout)

        # load initial list of a books
        self.load_books()
        return widget

    # loads book data from the repository and displays it in the table
    def load_books(self):
        # read search term or use None for all books
        term = self.catalog_search.text().strip() or None

        # fetch matching books from the database
        books = self.book_repo.get_all(term)

        # clear existing table contents
        self.catalog_table.setRowCount(0)

        # insert each book into the table row-by-row
        for row_idx, b in enumerate(books):
            self.catalog_table.insertRow(row_idx)
            self.catalog_table.setItem(row_idx, 0, QTableWidgetItem(str(b.id)))
            self.catalog_table.setItem(row_idx, 1, QTableWidgetItem(b.title))
            self.catalog_table.setItem(row_idx, 2, QTableWidgetItem(b.category or ""))
            self.catalog_table.setItem(row_idx, 3, QTableWidgetItem(str(b.published_year or "")))
            self.catalog_table.setItem(row_idx, 4, QTableWidgetItem(str(b.available_copies)))

    # --- Loans Tab (placeholder for you to extend) ---
    # placeholder loans tab (you can later add borrow/return workflow here)
    def _build_loans_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # display message for now until features are added
        layout.addWidget(QLabel("Loan workflows (borrow/return) go here."))
        widget.setLayout(layout)
        return widget

    # --- Clubs Tab (placeholder for you to extend) ---
    # placeholder for Book Clubs tab
    def _build_clubs_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # display message until UI is implemented
        layout.addWidget(QLabel("Book club management UI goes here."))
        widget.setLayout(layout)
        return widget

    # --- Dashboard Tab ---
    # builds the dashboard tab that displays system statistics
    def _build_dashboard_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        # get summary statistics from the database
        summary = self.dashboard_service.get_summary()

        # display system metrics
        layout.addWidget(QLabel(f"Total books: {summary['total_books']}"))
        layout.addWidget(QLabel(f"Total members: {summary['total_members']}"))
        layout.addWidget(QLabel(f"Active loans: {summary['active_loans']}"))
        layout.addWidget(QLabel(f"Overdue loans: {summary['overdue_loans']}"))

        # display top borrowed books
        layout.addWidget(QLabel("Top borrowed books:"))
        for row in summary["top_books"]:
            layout.addWidget(
                QLabel(f"- {row['title']} ({row['times_borrowed']} times)")
            )

        widget.setLayout(layout)
        return widget
