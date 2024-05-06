import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QPen

class DoubleBorderWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)
        self.outer_color = QColor(Qt.black)
        self.inner_color = QColor(Qt.red)
        self.outer_border_width = 10
        self.inner_border_width = 20

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Outer border
        painter.setPen(QPen(self.outer_color, self.outer_border_width))
        painter.drawRect(self.rect())

        # Inner border
        inner_rect = QRect(self.rect().topLeft() + QPoint(self.outer_border_width, self.outer_border_width),
                           self.rect().bottomRight() - QPoint(self.outer_border_width, self.outer_border_width))
        painter.setPen(QPen(self.inner_color, self.inner_border_width))
        painter.drawRect(inner_rect)

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    layout = QVBoxLayout()
    double_border_widget = DoubleBorderWidget()
    layout.addWidget(double_border_widget)
    widget.setLayout(layout)
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
