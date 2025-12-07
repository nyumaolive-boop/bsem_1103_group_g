from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QFormLayout, QLineEdit,
    QPushButton, QMessageBox
)
from services.auth_service import AuthService
from ui.main_window import MainWindow

# loginWindow handles user login using PyQt5 widgets
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set window title for the login screen
        self.setWindowTitle("SmartLibrary - Login")

        # service responsible for checking username & password
        self.auth_service = AuthService()

        # build the user interface layout (inputs & button)
        self._build_ui()

    def _build_ui(self):
        # main layout container
        layout = QVBoxLayout()

        # form layout holds the username/password input fields
        form = QFormLayout()

        # username field input
        self.username_input = QLineEdit()

        # password field input (characters hidden)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # add input field to the form layout
        form.addRow("Username:", self.username_input)
        form.addRow("Password:", self.password_input)

        # login button triggers the handle_login
        self.login_btn = QPushButton("Login")
        self.login_btn.clicked.connect(self.handle_login)

        # add form and login button to the main layout
        layout.addLayout(form)
        layout.addWidget(self.login_btn)

        # apply layout and set window size
        self.setLayout(layout)
        self.resize(300, 150)

    def handle_login(self):
        # retrieve input values from the UI
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        # attempt to authenticate user
        user = self.auth_service.login(username, password)

        # show warning if credentials are incorrect
        if not user:
            QMessageBox.warning(self, "Login failed", "Invalid credentials.")
            return

        # open the main application window on successful login
        self.main_window = MainWindow(user)
        self.main_window.show()

        # close the login window
        self.close()
