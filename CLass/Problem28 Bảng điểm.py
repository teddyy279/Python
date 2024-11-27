from math import*

class Student:
    def __init__(self, ID, name, scores):
        self.ID = str(ID)
        while len(self.ID) < 2:
            self.ID = '0' + self.ID
        self.ID = "HS" + self.ID
        self.name = name
        self.scores = scores[::]

    def average_score(self):
        return sum(self.scores) / 10
    
    def __str__(self):
        res = ""
        if self.average_score() >= 9:
            res = "XUAT XAC"
        if self.average_score() >= 8:
            res = "GIOI"
        if self.average_score() >= 7:
            res = "KHA"
        if self.average_score() >= 5:
            res = "TB"
        else:
            res = "YEU"

        return f'{self.ID} {self.name} {self.average_score():.1f} {res}'

    def get_ID(self):
        return self.ID

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        name = input()
        scores = list(map(float, input().split()))
        student = Student(i + 1, name, scores)
        a.append(student)
    
    a.sort(key = lambda x : -x.average_score())
    for x in a:
        print(x)
    
