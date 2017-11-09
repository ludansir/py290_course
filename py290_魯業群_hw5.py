#-*-coding:UTF-8 -*-
# 類別作業練習 EX05_hw.py
#
# 測試資料 http://140.112.31.82/wordpress/?p=216

class student:

    def __init__(self, n, g):
        self.name = n
        self.gender = g
        self.grades = []

    def add(self, grades):
        self.grades.append(grades)

    def avg(self):
        sum = 0
        for score in self.grades:
            sum += score
        print(self.name + ' AVG:'+ str(sum/len(self.grades)))
        

    def fcount(self):
        for score in self.grades:
            if score > 60:
                print(self.name + ' PASS:'+ str(score))
            else:
                print(self.name + ' FAILED:'+ str(score))

def top(name,*scores):
    for score in scores:
        print(name + ':' + str(score) + ',and the highest is ' + str(max(score)) + '.')
        

s1 = student("Tom","M")
s2 = student("Jane","F")
s3 = student("John","M")
s4 = student("Ann","F")
s5 = student("Peter","M")
s1.add(80)
s1.add(90)
s1.add(55)
s1.add(77)
s1.add(40)
s2.add(58)
s2.add(87)
s3.add(100)
s3.add(80)
s4.add(40)
s4.add(55)
s5.add(60)
s5.add(60)
s1.fcount()
s2.fcount()
s3.fcount()
s4.fcount()
s5.fcount()
s1.avg()
s2.avg()
s3.avg()
s4.avg()
s5.avg()
top(s1.name,s1.grades)
top(s2.name,s2.grades)
top(s3.name,s3.grades)
top(s4.name,s4.grades)
top(s5.name,s5.grades)
