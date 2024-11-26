class Teacher:
    def __init__(self, ID, name, base_salary):
        self.ID = ID
        self.name = name
        self.base_salary = base_salary
    def get_he_so(self):
        return int(ID[2:])
    def total_income(self):
        he_so = self.get_he_so()
        salary = self.base_salary * he_so
        cv = ID[0 : 2]
        if cv == 'HT':
            return 2000000 + salary
        elif cv == 'HP':
            return 900000 + salary
        else:
            return 500000 + salary
    def __str__(self):
        return f'{self.ID} {self.name} {self.get_he_so()} {self.total_income()}'


if __name__ == '__main__':
    ID = input()
    name = input()
    base_salary = int(input())
    Teacher = Teacher(ID, name, base_salary)
    Teacher.get_he_so()
    Teacher.total_income()
    print(Teacher)
