import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPlainTextEdit
from PyQt5.QtCore import Qt

class ResultDisplay(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.text_edit = QPlainTextEdit()
        filename = 'temp_data/result.txt'
        if filename:
            with open(filename, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.layout().addWidget(self.text_edit)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ResultDisplay()
    sys.exit(app.exec_())