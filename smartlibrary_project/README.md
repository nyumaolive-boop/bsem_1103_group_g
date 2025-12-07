# SmartLibrary – Final Project

SmartLibrary is a *desktop library management system* for Limkokwing University.

It is built with:

- *Python (OOP)* – for the logic and classes (Book, User, Loan, etc.)
- *PostgreSQL* – to store all data (books, users, members, loans, book clubs)
- *PyQt5* – to create the desktop windows (login screen, tabs, tables)
- *psycopg2* – to connect Python to PostgreSQL

This project is a *skeleton* that you can run, test, and then extend with more features.

---

## 1. Main Features in This Version

Right now, this system already has:

### 1.1 Login

- You can log in with a *username* and *password*.
- The system checks the users table in PostgreSQL.
- The demo data includes:
  - Librarian user: librarian / admin123
  - Student user: student / admin123

### 1.2 Main Window (PyQt5)

After login, you see the *main SmartLibrary window* with 4 tabs:

1. *Book Catalog*
   - Search books by title.
   - See a table with:
     - ID  
     - Title  
     - Category  
     - Year  
     - Available copies  

2. *Loans* (placeholder for now)
   - This tab is ready for you to add “Borrow” and “Return” features.

3. *Book Clubs* (placeholder for now)
   - This tab is ready for you to add club creation and member management.

4. *Dashboard*
   - Shows:
     - Total books  
     - Total members  
     - Number of active loans  
     - Number of overdue loans  
   - Shows a small list of *Top borrowed books* (from the loans table).

> The system is designed using *layers*: models, repositories, services, and UI.

---

## 2. Project Structure

```text
smartlibrary/
  app.py              # Main entry point (run this file)
  db.py               # PostgreSQL connection
  requirements.txt    # Python dependencies
  README.md           # This file

  models/
    user.py           # User class
    book.py           # Book class
    loan.py           # Loan class
    bookclub.py       # BookClub class

  repositories/
    user_repo.py      # Read users from DB, password verify
    book_repo.py      # Read books from DB (for catalog)
    loan_repo.py      # Helpers for loans
    club_repo.py      # Helpers for book clubs

  services/
    auth_service.py       # Login logic
    loan_service.py       # Business rules for loans
    dashboard_service.py  # Summary statistics for dashboard

  ui/
    login_window.py   # Login screen (PyQt5)
    main_window.py    # Main window with tabs (PyQt5)