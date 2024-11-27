class Student:
    def __init__(self, ID, name, class_name, birth_of_date, gpa):
        self.ID = str(ID)
        while len(self.ID) < 3:
            self.ID = '0' + self.ID
        self.ID = "SV" + self.ID
        self.name = name
        self.class_name = class_name
        self.birth_of_date = birth_of_date
        self.gpa = gpa
     
    def normalize_name(self):
        self.name = self.name.title()
    
    def normalize_birth_of_date(self):
        if self.birth_of_date[1] == '/':
            self.birth_of_date = '0' + self.birth_of_date
        if self.birth_of_date[4] == '/':
            self.birth_of_date = self.birth_of_date[0 : 3] + '0' + self.birth_of_date[3 :]
    
    def __str__(self):
        return f'{self.ID} {self.name} {self.class_name} {self.birth_of_date} {self.gpa:.2f}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        student = Student(i + 1, input(), input(), input(), float(input()))
        student.normalize_name()
        student.normalize_birth_of_date()
        a.append(student)
    
    for x in a:
        print(x)
