class Student:
    def __init__(self, ID, name, class_name, email):
        self.ID = ID
        self.name = name
        self.class_name = class_name
        self.email = email
    
    def __str__(self):
        return f'{self.ID} {self.name} {self.class_name} {self.email}'

    def get_class_name(self):
        return self.class_name

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        student = Student(input(), input(), input(), input())
        a.append(student)
    
    a.sort(key = lambda x : x.get_class_name())
    for x in a:
        print(x)
