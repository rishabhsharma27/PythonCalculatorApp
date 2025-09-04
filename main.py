# Import Modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QApplication, QWidget, QLabel, QPushButton, QGridLayout, QLineEdit
#from random import choice

# Main App Object and Settings


# Create all App Object
class CalcApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.resize(250, 300)
        #title = QLabel("Cal")

        # All widgets 
        self.text_box = QLineEdit()
        self.grid = QGridLayout()

        self.Opers_char = "7 8 9 / " \
                    "4 5 6 * " \
                    "1 2 3 - " \
                    "0 . = +" 
        self.buttons = self.Opers_char.split(" ")

        col = 0
        row = 0
        for text in self.buttons:
            #print(text)
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col = col + 1
            if col > 3:
                col = 0
                row = row + 1

        self.clear = QPushButton("Clear")

        self.delete = QPushButton("<")

        # All Design Here
        master_layout = QVBoxLayout()

        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)

        self.setLayout(master_layout)

        # Events
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

        # Create Functions
    def button_click(self):
        button = app.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try: 
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error", e)  

        elif text == "Clear":
            self.text_box.clear()

        elif text == "<":
            current_val = self.text_box.text()
            self.text_box.setText(current_val[:-1])

        else:
            current_val = self.text_box.text()
            self.text_box.setText(current_val + text )



# Show/Run our App'
if __name__ in "__main__":
    app = QApplication([])
    main_window = CalcApp()
    main_window.show()
    app.exec_()
