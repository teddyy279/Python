class Person:
    def __init__(self, fullname, date_of_birth, address):
        self.fullname = fullname
        self.date_of_birth = date_of_birth
        self.address = address

    def normalize_date_of_birth(self):
        if self.date_of_birth[1] == '/':
            self.date_of_birth = '0' + self.date_of_birth
        if self.date_of_birth[4] == '/':
            self.date_of_birth = self.date_of_birth[:3] + '0' + self.date_of_birth[3:]
    
    def normalize_fullname(self):
        self.fullname = self.fullname.title()

    def __str__(self):
        return f'{self.fullname} {self.date_of_birth} {self.address}'

class Student(Person):
    def __init__(self, ID, fullname, date_of_birth, address, major, gpa):
        Person.__init__(self, fullname, date_of_birth, address)
        self.ID = str(ID)
        while len(self.ID) < 4:
            self.ID = "0" + self.ID
        self.major = major
        self.gpa = float(gpa)
        self.normalize_fullname()
        self.normalize_date_of_birth()

    def __str__(self):
        return f'{self.ID} {super().__str__()} {self.major} {self.gpa:.2f}'

def compare_name(s):
    a = s.split()
    res = a[-1] + ' '
    res += ' '.join(a[:-1])
    return res

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        student = Student(i + 1, input(), input(), input(), input(), float(input()))
        a.append(student)
    
    a.sort(key=lambda x: compare_name(x.fullname))
    for x in a:
        print(x)
