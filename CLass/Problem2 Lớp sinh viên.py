class Student:
    def __init__(self, name, date_of_birth, score1, score2, score3):
        self.name = name
        self.date_of_birth = date_of_birth
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def __str__(self):
        totalScore = score1 + score2 + score3
        return f'{self.name} {self.date_of_birth} {totalScore:.1f}'

if __name__ == '__main__':
    name = input()
    date_of_birth = input()
    score1 = float(input())
    score2 = float(input())
    score3 = float(input())
    Student = Student(name, date_of_birth, score1, score2, score3)
    print(Student)
