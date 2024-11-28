class Student:
    def __init__(self, ID, name, class_name, email):
        self.ID = ID
        self.name = name
        self.class_name = class_name
        self.email = email

    def normalize_name(self):
        self.name = self.name.title()
    
    def __str__(self):
        return f'{self.ID} {self.name} {self.class_name} {self.email}'

    def get_course_year(self):
        return self.ID[:4]

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        student = Student(input(), input(), input(), input())
        student.normalize_name()
        a.append(student)
    
    t  = int(input())
    for _ in range(t):
        q = input()
        print("DANH SACH SINH VIEN KHOA", q, ":")
        for x in a:
            if q == x.get_course_year():
                print(x)
