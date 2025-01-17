class Person:
    def __init__(self, ID, name, birth_of_date, address):
        self.ID = ID
        self.name = name
        self.birth_of_date = birth_of_date
        self.address = address
    
    def normalize_name(self):
        self.name = self.name.title()

    def normalize_birth_of_date(self):
        if self.birth_of_date[1] == '/':
            self.birth_of_date = "0" + self.birth_of_date
        if self.birth_of_date[4] == '/':
            self.birth_of_date = self.birth_of_date[:3] + '0' + self.birth_of_date[3:]

    def __str__(self):
        return self.ID + ' ' + self.name + ' ' + self.birth_of_date + ' ' + self.address

    def get_address(self):
        return self.address

class Student(Person):
    def __init__(self, ID, name, birth_of_date, address, class_name, gpa):
        Person.__init__(self, ID, name, birth_of_date, address)
        self.class_name = class_name
        self.gpa = gpa
        self.normalize_name()
        self.normalize_birth_of_date()

    def __str__(self):
        return Person.__str__(self) + ' ' + self.class_name + ' ' + '{:.2f}'.format(self.gpa)

class Teacher(Person):
    def __init__(self, ID, name, birth_of_date, address, faculty, salary, class_name):
        Person.__init__(self, ID, name, birth_of_date, address)
        self.faculty = faculty
        self.salary = salary
        self.class_name = class_name
        self.normalize_birth_of_date()
        self.normalize_name()

    def __str__(self):
        return Person.__str__(self) + ' ' + self.faculty + ' ' + self.class_name + str(self.salary)

if __name__ == '__main__':
    n = int(input())
    teacher, student = [], []
    for _ in range(n):
        ID = input()
        if ID[:2] == "GV":
            name = input()
            birth_of_date = input()
            address = input()
            faculty = input()
            salary = input()
            class_name = input()
            t = Teacher(ID, name, birth_of_date, address, faculty, salary, class_name)
            t.normalize_birth_of_date()
            t.normalize_name()
            teacher.append(t)
        else:
            name = input()
            birth_of_date = input()
            address = input()
            class_name = input()
            gpa = float(input())
            s = Student(ID, name, birth_of_date, address, class_name , gpa)
            s.normalize_birth_of_date()
            s.normalize_name()
            student.append(s)

    address = input()
    print('DANH SACH SINH VIEN CO DIA CHI TAI ' + address + ':')
    for x in teacher:
        if(address == x.get_address()):
            print(x)
    print('DAnh SACH GIAO VIEN CO DIA CHI TAI ' + address + ':')
    for x in student:
        if(address == x.get_address()):
            print(x)
