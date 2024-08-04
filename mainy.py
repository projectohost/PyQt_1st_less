from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import randint

app = QApplication ([])

# головне вікно програми
my_p = QWidget()
my_p.setWindowTitle("Визначник переможця")
my_p.resize(400,200)

# віджети програми(всі об'єкти)
button = QPushButton('Згенерувати')
text = QLabel('Натисніть на кнопку, щоб знайти переможця!')
winner = QLabel('?')

# розташування для наших об'єктів
line = QVBoxLayout()

line.addWidget(text, alignment= Qt.AlignCenter)
line.addWidget(winner, alignment= Qt.AlignCenter)
line.addWidget(button, alignment= Qt.AlignCenter)

my_p.setLayout(line)  # щоб відобразити всі наші віджети

# генерація випадкового числа
def show_winner():
    num = randint(0,99)
    winner.setText(str(num))   # замість '?' ставиться переможне число
    text.setText('Переможець:')

button.clicked.connect(show_winner)

app.setStyleSheet('''QWidget{
                  font-size: 40px;
                  background: lightgreen;
                  }
                  
                  QPushButton:hover{
                  color: blue;
                  }''')
my_p.show()
app.exec()