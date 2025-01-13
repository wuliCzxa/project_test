import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QMainWindow, QTextEdit
from test_01 import CinemaDataProcessor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cinema Management System - Main Window')
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.label = QLabel('Welcome to Cinema Management System')
        self.layout.addWidget(self.label)

class DataManipulationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cinema Management System - Data Manipulation')
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 200)

        self.username_label = QLabel('Username:')
        self.username_input = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('Login')
        self.login_button.clicked.connect(self.login_user)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        self.setLayout(self.layout)

    def login_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        if username and password:
            if cinema.login_user(username, password):
                self.open_data_manipulation_window()
            else:
                QMessageBox.warning(self, 'Login', 'Username or password incorrect.')
        else:
            QMessageBox.warning(self, 'Login', 'Please enter username and password.')

    def open_data_manipulation_window(self):
        self.test_window = cinema()
        self.test_window.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
