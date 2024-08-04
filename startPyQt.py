from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, 
QPushButton, QLabel, QVBoxLayout, QHBoxLayout)
from random import randint

app = QApplication([])    # створюємо програму

my_w = QWidget()
my_w.setWindowTitle('Визначник переможця')
my_w.resize(400,200)

# кнопка
button = QPushButton('Згенерувати')
text = QLabel('Натисніть, щоб дізнатись переможця')
winner = QLabel('?')

# розташування 
line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
my_w.setLayout(line)

def random():
    number = randint(0,99)
    winner.setText(str(number))
    text.setText('Переможець:')

button.clicked.connect(random)

app.setStyleSheet('''
QWidget{
    font-size: 30px;  
    background: lightgrey;     
}
QPushButton:hover{
    background: lightblue;
}
''')
my_w.show()
app.exec()
