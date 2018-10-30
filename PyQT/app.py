import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        #метод super() принудительно вызывает родительский конструктор(QWidget)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Arial', 20))
        self.setToolTip('typical')    #шаблон

        btn = QPushButton('Push me', self)
        btn.setToolTip('This is just a simple button')
        btn.resize(btn.sizeHint())    #SizeHint дает рекомендуемый размер кнопки
        btn.move(50, 50)    #перемещение относительно окна

        quit_btn = QPushButton('QUIT IS HERE', self)
        quit_btn.clicked.connect(QCoreApplication.instance().quit)
        quit_btn.resize(btn.sizeHint())
        quit_btn.move(150, 50)

        self.setGeometry(300, 300, 300, 220)    #первые два - положение;ширина и высота
        self.setWindowTitle('first app')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
