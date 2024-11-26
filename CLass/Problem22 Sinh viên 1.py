class Student:
    def __init__(self, ID, name, major, birth_of_date, gpa):
        self.ID = str(ID)
        while len(self.ID) < 3:
            self.ID = '0' + self.ID
        self.ID = "SV" + self.ID
        self.name = name 
        self.major = major
        self.birth_of_date = birth_of_date
        self.gpa = gpa
    
    def __str__(self):
        return f'{self.ID} {self.name} {self.major} {self.birth_of_date} {self.gpa:.1f}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        student = Student(i + 1, input(), input(), input(), float(input()))
        a.append(student)
    for x in a:
        print(x) 
