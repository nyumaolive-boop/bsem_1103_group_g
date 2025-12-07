import sys
from PyQt5.QtWidgets import QApplication
from ui.login_window import LoginWindow

def main():
    """
    Entry point of the  smartlibrary application.
    Create the Qt application, opens the login window,
    and starts the event loop.
    """
    # create a QApplication object - requirement for any PyQt program
    app = QApplication(sys.argv)

    # create and display the login window
    window = LoginWindow()
    window.show()

    # start the Qt event loop and exit cleanly when the app closes
    sys.exit(app.exec_())

# ensure this file runs as the main program (not when imported as a module)
if __name__ == "__main__":
    main()

