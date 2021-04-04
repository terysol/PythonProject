import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
import subprocess

class start(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        font1 = QtGui.QFont('나눔바른고딕', 10)
        font1.setBold(True)
        self.title = QLabel("누구세요", self)
        self.title.move(230, 100)
        self.title.resize(400, 100)
        self.title.setFont(QtGui.QFont('나눔바른고딕', 60))
        self.title.setStyleSheet("color:white")
        # 폰트 사이즈, 폰트 지정
        self.setStyleSheet("background:rgb(91,153,250)")

        self.startBtn = QPushButton('시작', self)
        self.startBtn.move(320, 260)
        self.startBtn.resize(150, 50)
        self.startBtn.setFont(font1)
        self.startBtn.clicked.connect(self.startBtn_clicked)
        self.startBtn.setStyleSheet("background:white")

        self.graphBtn = QPushButton('그래프 보기', self)
        self.graphBtn.move(320, 320)
        self.graphBtn.resize(150, 50)
        self.graphBtn.setFont(font1)
        self.graphBtn.clicked.connect(self.graphBtn_clicked)
        self.graphBtn.setStyleSheet("background:white")

        self.setWindowTitle("누구세요")
        self.resize(800, 500)
        self.show()

    def startBtn_clicked(self):
        subprocess.call("StudentUI.py", shell=True)

    def graphBtn_clicked(self):
        subprocess.call("Graph.py", shell=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = start()

    sys.exit(app.exec_())