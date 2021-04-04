import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, \
    QDesktopWidget
from PyQt5 import QtGui
from Student import Student

class StudentUI(QWidget):

    def __init__(self):
        super().__init__()
        self.student=Student()
        self.initUI()

    # QMainWindow
    def initUI(self):  # 버튼 배열 gridLayout 으로 바꾸기
        font1 = QtGui.QFont()
        font1.setBold(True)
        self.setStyleSheet("background:rgb(91,153,250)")

        self.btn1 = QPushButton('1', self)
        self.btn1.toggle()
        self.btn1.resize(70,70)
        self.btn1.setFont(font1)
        self.btn1.clicked.connect(lambda state,button=self.btn1:self.NumClicked(state,button))
        self.btn1.setStyleSheet("background:white")

        self.btn2 = QPushButton('2', self)
        self.btn2.toggle()
        self.btn2.resize(70, 70)
        self.btn2.setFont(font1)
        self.btn2.clicked.connect(lambda state,button=self.btn2:self.NumClicked(state,button))
        self.btn2.setStyleSheet("background:white")

        self.btn3 = QPushButton('3', self)
        self.btn3.toggle()
        self.btn3.resize(70, 70)
        self.btn3.setFont(font1)
        self.btn3.clicked.connect(lambda state,button=self.btn3:self.NumClicked(state,button))
        self.btn3.setStyleSheet("background:white")

        self.btn4 = QPushButton('4', self)
        self.btn4.toggle()
        self.btn4.resize(70, 70)
        self.btn4.setFont(font1)
        self.btn4.clicked.connect(lambda state,button=self.btn4:self.NumClicked(state,button))
        self.btn4.setStyleSheet("background:white")

        self.btn5 = QPushButton('5', self)
        self.btn5.toggle()
        self.btn5.resize(70, 70)
        self.btn5.setFont(font1)
        self.btn5.clicked.connect(lambda state,button=self.btn5:self.NumClicked(state,button))
        self.btn5.setStyleSheet("background:white")

        self.btn6 = QPushButton('6', self)
        self.btn6.toggle()
        self.btn6.resize(70, 70)
        self.btn6.setFont(font1)
        self.btn6.clicked.connect(lambda state,button=self.btn6:self.NumClicked(state,button))
        self.btn6.setStyleSheet("background:white")

        self.btn7 = QPushButton('7', self)
        self.btn7.toggle()
        self.btn7.resize(70, 70)
        self.btn7.setFont(font1)
        self.btn7.clicked.connect(lambda state,button=self.btn7:self.NumClicked(state,button))
        self.btn7.setStyleSheet("background:white")

        self.btn8 = QPushButton('8', self)
        self.btn8.toggle()
        self.btn8.resize(70, 70)
        self.btn8.setFont(font1)
        self.btn8.clicked.connect(lambda state,button=self.btn8:self.NumClicked(state,button))
        self.btn8.setStyleSheet("background:white")

        self.btn9 = QPushButton('9', self)
        self.btn9.toggle()
        self.btn9.resize(70, 70)
        self.btn9.setFont(font1)
        self.btn9.clicked.connect(lambda state,button=self.btn9:self.NumClicked(state,button))
        self.btn9.setStyleSheet("background:white")

        self.btn0 = QPushButton('0', self)
        self.btn0.toggle()
        self.btn0.resize(70, 70)
        self.btn0.setFont(font1)
        self.btn0.clicked.connect(lambda state,button=self.btn0:self.NumClicked(state,button))
        self.btn0.setStyleSheet("background:white")

        self.check=QPushButton('확인',self)
        self.check.toggle()
        self.check.resize(70,70)
        self.check.setFont(font1)
        self.check.clicked.connect(self.check_num)
        self.check.setStyleSheet("background:white")

        self.delete=QPushButton('지우기',self)
        self.delete.toggle()
        self.delete.resize(70,70)
        self.delete.setFont(font1)
        self.delete.clicked.connect(self.one_delete)
        self.delete.setStyleSheet("background:white")

        self.finish=QPushButton('학생 끝',self)
        self.finish.toggle()
        self.finish.resize(80,30)
        self.finish.setFont(font1)
        self.finish.clicked.connect(self.check_save)
        self.finish.setStyleSheet("background:white")

        self.line_edit = QLineEdit('',self)
        self.line_edit.resize(180,40)
        self.line_edit.move(165,40)
        font=QtGui.QFont()
        font.setBold(True)
        font.setPointSize(18)
        self.line_edit.setFont(font)
        self.line_edit.setFont(font)
        self.line_edit.setStyleSheet("background-color:white")

        self.btn1.move(150,100)
        self.btn2.move(220,100)
        self.btn3.move(290,100)

        self.btn4.move(150, 170)
        self.btn5.move(220,170)
        self.btn6.move(290,170)

        self.btn7.move(150,240)
        self.btn8.move(220,240)
        self.btn9.move(290,240)

        self.delete.move(150, 310)
        self.btn0.move(220,310)
        self.check.move(290, 310)
        self.finish.move(215,385)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('누구세요')  # 제목
        self.center()
        self.show()  # 스크린에 보여줌

    # def make_button(self,index):
    #     button=QPushButton(str(index),self)
    def NumClicked(self,state,button):
        line_edit_text = self.line_edit.text()
        self.line_edit.setText(line_edit_text + button.text())

    def one_delete(self):
        arr=self.line_edit.text()
        self.line_edit.setText(arr[0:-1])

    def check_num(self):  # 만들어야 하는 조건 : 이미 카운트 된 이름이라면 또 다시 눌렸을 때 "이미 확인되었습니다" 라고 띄우기
        hakbun = self.line_edit.text()
        self.student.file()
        self.name = self.student.select(hakbun)
        if hakbun in self.student.student.keys():
            self.msg = QMessageBox.about(self, "QMessageBox", f'{self.name}님 확인 되셨습니다.')
        else:
            self.msg2 = QMessageBox.warning(self, "QMessageBox", "저장되지 않은 학생입니다.")
        if hakbun == '':
            self.message = QMessageBox.warning(self, "QMessageBox", "학번을 입력해주세요.")
        self.line_edit.setText('')

    def check_save(self):
        self.student.save()
        self.m=QMessageBox.about(self,'QMessageBox','저장되었습니다.')

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StudentUI()
    sys.exit(app.exec_())