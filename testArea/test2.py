import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QEvent, QUrl
from PyQt5.QtGui import QDesktopServices

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Open Link Example")
        self.setGeometry(100, 100, 400, 200)

        # Create a QVBoxLayout to hold the text edit
        layout = QVBoxLayout()

        # Create a QTextEdit
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setHtml("<a href='http://www.example.com'>Click me to open link</a><br>dasfdsf")

        # Disable text interaction to avoid editing
        text_edit.setTextInteractionFlags(Qt.TextBrowserInteraction)

        # Install an event filter to intercept mouse clicks on links
        text_edit.viewport().installEventFilter(self)

        # Add the text edit to the layout
        layout.addWidget(text_edit)

        # Create a central widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseButtonPress and obj.anchorAt(event.pos()):
            link = obj.anchorAt(event.pos())
            QDesktopServices.openUrl(QUrl(link))
            return True
        return super().eventFilter(obj, event)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
