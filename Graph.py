import sys
from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
from PyQt5 import QtGui
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import datetime
from Student import Student
import pandas as pd

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.student = Student()
        self.initUI()
        self.setLayout(self.layout)
        self.setGeometry(200, 200, 800, 600)

    def initUI(self):
        font1 = QtGui.QFont('나눔바른고딕')
        font1.setBold(True)
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        self.setWindowTitle('누구세요')
        self.setStyleSheet("background:rgb(91,153,250)")
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.cb = QComboBox()
        self.cb.setStyleSheet('background-color:white')
        self.cb.setFont(font1)
        self.cb.addItem('일별')
        self.cb.addItem('주별')
        self.cb.activated[str].connect(self.onComboBoxChanged)
        layout.addWidget(self.cb)
        self.layout = layout
        self.onComboBoxChanged(self.cb.currentText())

    def onComboBoxChanged(self, text):
        if text == '일별':
            self.day_count_student()
        elif text == '주별':
            self.week_count_student()

    def chage_date(self):
        d = self.student.date
        t = datetime.datetime.strptime(d, '%Y-%m-%d')
        last_monday = t - datetime.timedelta(days=t.weekday())
        cal = last_monday.isocalendar()
        day_week = cal[1]
        return day_week

    def day_count_student(self):  # 일별 그래프
        student = {}
        with open('today_student.txt', 'r', encoding='utf8') as f:
            data = f.readlines()
            for voc in data:
                voc = voc.strip().split('\t')
                student[voc[0]] = voc[1]

        row = []
        column = []
        for line in data:
            line = line.split('\t')
            row.append(line[0])

        dic = {}
        i = self.chage_date()

        for r in row:
            t = datetime.datetime.strptime(r, '%Y-%m-%d')
            last = t - datetime.timedelta(days=t.weekday())
            c = last.isocalendar()
            dic.setdefault(r, c[1])

        li = []
        for date, num in dic.items():
            if num == i:
                li.append(date)
        for l in li:
            if l in student.keys():
                column.append(int(student.get(l)))

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        ax.set_ylim(0, 10)
        rects = ax.bar(li, column, label="student")

        ax.set_xlabel("date")
        ax.set_title("Student")
        ax.legend()

        self.canvas.draw()
        for i, rect in enumerate(rects):
            ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * rect.get_height(), str(column[i]),
                    ha='center')

    def week_count_student(self):  # 주별 그래프
        df = pd.read_csv(open("today_student.txt", "rb"), delimiter='\t')
        df.columns = ['date', 'cnt']

        df['datetime'] = df['date'].apply(lambda x: pd.to_datetime(str(x), format='%Y-%m-%d'))
        df.set_index(df['datetime'], inplace=True)

        weekly_df = pd.DataFrame()
        weekly_df['cnt'] = df['cnt'].resample('W-Fri').sum().fillna(0)
        for i in range(len(weekly_df.index)):
            weekly_df['date'] = weekly_df['cnt'].index

        name = []
        values = []

        for i in range(len(weekly_df['cnt'])):
            values.append(weekly_df.cnt[i])

        for i in range(len(weekly_df['date'])):
            date = weekly_df.date[i]
            s = date.strftime('%Y-%m-%d')
            name.append(s)

        self.fig.clear()
        ax = self.fig.add_subplot(111)
        rects = ax.bar(name, values, label="student")
        ax.set_xlabel("week")
        ax.set_title("Student")
        ax.legend()

        self.canvas.draw()

        for i, rect in enumerate(rects):
            ax.text(rect.get_x() + rect.get_width() / 2.0, 1.05 * rect.get_height(), str(weekly_df.cnt[i]),
                    ha='center')

    def center(self): #화면 가운데에 띄우기 위해서
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.center()
    window.show()
    app.exec_()