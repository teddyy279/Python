class Student:
    def __init__(self, Id, name, class_name, date_of_birth, gpa):
        self.Id = Id
        self.name = name
        self.class_name = class_name
        self.date_of_birth = date_of_birth
        self.gpa = gpa
    def normalize_date_birth(self):
        if self.date_of_birth[1] == '/':
            self.date_of_birth = '0' + self.date_of_birth
        if self.date_of_birth[4] == '/':
            self.date_of_birth = self.date_of_birth[0 : 3] + '0' + self.date_of_birth[3 :]
    def __str__(self):
        return f'{self.Id} {self.name} {self.class_name} {self.date_of_birth} {self.gpa:.1f}'


if __name__ == '__main__':
    name = input()
    class_name = input()
    date_of_birth = input()
    gpa = float(input())
    Student = Student("SV001", name, class_name, date_of_birth, gpa)
    Student.normalize_date_birth()
    print(Student)
