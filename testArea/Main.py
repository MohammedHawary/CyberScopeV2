import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.last_pressed_button = None  # Variable to store the last pressed button

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        button1 = QPushButton("Button 1")
        layout.addWidget(button1)

        button2 = QPushButton("Button 2")
        layout.addWidget(button2)

    def button_clicked(self, button):
        self.last_pressed_button = button
        QMessageBox.information(self, "Button Clicked", f"{button.text()} clicked.")

    def closeEvent(self, event):
        print("Last pressed button:", self.last_pressed_button.text() if self.last_pressed_button else "None")
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
