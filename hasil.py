import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QInputDialog
)

class InputDialogDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog demo")
        self.setGeometry(100, 100, 400, 150)

        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        self.label_list = QLabel("Choose from list")
        self.button_list = QPushButton("")  # default
        self.button_list.clicked.connect(self.get_item)
        row1.addWidget(self.label_list)
        row1.addWidget(self.button_list)
        main_layout.addLayout(row1)

        row2 = QHBoxLayout()
        self.label_name = QLabel("get name")
        self.button_name = QPushButton("")  # default
        self.button_name.clicked.connect(self.get_text)
        row2.addWidget(self.label_name)
        row2.addWidget(self.button_name)
        main_layout.addLayout(row2)

        row3 = QHBoxLayout()
        self.label_int = QLabel("Enter an integer")
        self.button_int = QPushButton("")  # default
        self.button_int.clicked.connect(self.get_integer)
        row3.addWidget(self.label_int)
        row3.addWidget(self.button_int)
        main_layout.addLayout(row3)

        self.setLayout(main_layout)

    def get_item(self):
        items = ("C", "C++", "Java", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", 
                                        "List of languages:", items, 0, False)
        if ok and item:
            self.button_list.setText(item)

    def get_text(self):
        text, ok = QInputDialog.getText(self, "Text Input Dialog", "Enter your name:")
        if ok and text:
            self.button_name.setText(text)

    def get_integer(self):
        number, ok = QInputDialog.getInt(self, "Integer Input Dialog", "Enter a number:")
        if ok:
            self.button_int.setText(str(number))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = InputDialogDemo()
    demo.show()
    sys.exit(app.exec_())
