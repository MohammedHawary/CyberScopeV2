from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QAction, QPushButton, QLabel
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtGui import QIcon

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        uic.loadUi('LoginWindow.ui', self)
        self.load_stylesheet("LoginWindow.qss")
                    # initialize UI elements from UI file
                            # QWidget
        self.loginWidget   = self.findChild(QWidget, "loginWidget")
                            # QLineEdit
        self.userNameInput = self.findChild(QLineEdit, "userNameInput")
        self.passwordInput = self.findChild(QLineEdit, "passwordInput")
                            # QPushButton
        self.signInbtn = self.findChild(QPushButton, "signInbtn")
                            # QLabel
        self.uncorerctMessageLabel = self.findChild(QLabel, "uncorerctMessageLabel")
                            # QLineEdit section
        self.userNameInput.setClearButtonEnabled(True)
        self.passwordInput.setClearButtonEnabled(True)
        self.userNameInput.addAction(QIcon("png/username.png"),QLineEdit.ActionPosition.LeadingPosition)
        self.passwordInput.addAction(QIcon("png/password.png"),QLineEdit.ActionPosition.LeadingPosition)
        self.userNameInput.findChildren(QAction)[0].setIcon(QIcon("png/clear.png"))
        self.passwordInput.findChildren(QAction)[0].setIcon(QIcon("png/clear.png"))
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.userNameInput.setPlaceholderText("Username")
        self.passwordInput.setPlaceholderText("Password")
        self.userNameInput.setFocus()

                            # QPushButton section
        self.signInbtn.clicked.connect(self.on_signIn_button_clicked)
        self.passwordInput.returnPressed.connect(lambda: self.signInbtn.click())


        self.show()


    def on_signIn_button_clicked(self):
        # This method will be called when the login button is clicked
        username = self.userNameInput.text()
        password = self.passwordInput.text()
        defualtUserName = "admin"
        defualtpassword = "admin"
        if username == defualtUserName and password == defualtpassword:
            self.uncorerctMessageLabel.setText("")
        else:
            self.uncorerctMessageLabel.setText("Username or Password Uncorrect !")


    def load_stylesheet(self, filename):
        # Read the content of the QSS file
        style_file = QFile(filename)
        if style_file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(style_file)
            content = stream.readAll()
            style_file.close()
            # Apply the stylesheet to the main window
            self.setStyleSheet(content)
        else:
            print(f"Failed to open {filename}")

app = QApplication([])
UiWindow = LoginWindow()
app.exec_()
