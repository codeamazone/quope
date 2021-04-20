import sys
import requests
import json

from pathlib import Path
import PyQt5.QtWidgets as pw
from quotes import get_quote


class Window(pw.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(200, 400)
        self.setWindowTitle('quope')

        ## WIDGETS ##
        self.text = pw.QLabel('Do you need some inspiration?')
        self.quote_button = pw.QPushButton('Give me my quote!')
        self.quote_button.clicked.connect(lambda: self.get_quote())
        self.quotefield = pw.QTextEdit()
        self.quotefield.setPlaceholderText('Your space for inspiration')

        ## LAYOUT ##
        hBox = pw.QVBoxLayout()
        hBox.addWidget(self.text)
        hBox.addWidget(self.quote_button)
        hBox.addWidget(self.quotefield)
        self.setLayout(hBox)

        self.show()

    def get_quote(self):
        resp = requests.get(
            'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en')
        try:
            # print(resp.status_code == 200)
            quote = resp.json()['quoteText']
            # return quote
        except Exception:
            quote = 'Something went wrong'
        self.quotefield.setText(quote)
        self.quotefield.repaint()


if __name__ == '__main__':
    app = pw.QApplication(sys.argv)
    p = Path(__file__).parent / 'style.css'
    app.setStyleSheet(open(p).read())
    w = Window()
    sys.exit(app.exec_())
