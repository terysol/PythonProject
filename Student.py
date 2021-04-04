import datetime

class Student:
    def __init__(self):
        self.date=datetime.datetime.now().strftime('%Y-%m-%d')
        self.name=''
        self.number=0
        self.student={}
        self.today_count=0

    def select(self, number):
        self.file()
        for v in self.student.keys():
            if number == v:
                self.name = self.student.get(v)
                self.today_count += 1
            else:
                continue
        return self.name

    def file(self):
        result = open('studentinfo.txt', 'r', encoding='utf8')
        for voc in result:
            voc = voc.strip().split('\t')
            self.student[voc[0]] = voc[1]
        result.close()

    def save(self):
        f=open('today_student.txt','a',encoding='utf8')
        f.write(self.date + '\t'+ str(self.today_count) + '\n')
        f.close()


    def __str__(self):
        return f'오늘 날짜 : {self.date}\t 총 인원 : {self.today_count}'


if __name__ == '__main__':
    s=Student()
    while True:
        number = input("학번을 입력하세요. >> ")
        if number=='exit':
            #s.save()
            break
        s.select(number)

    print(s)
