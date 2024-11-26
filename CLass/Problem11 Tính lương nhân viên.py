class Employee:
    def __init__(self, ID, name, base_salary, working_days, position):
        self.ID = ID
        self.name = name 
        self.base_salary = base_salary
        self.working_days = working_days  # Fixed typo
        self.position = position

    def calculate_salary(self):
        return self.base_salary * self.working_days
    
    def calculate_bonus(self):
        salary = self.calculate_salary()  # Calculate salary once
        if self.working_days >= 25:  # Use self.working_days
            return salary * 20 / 100
        elif self.working_days >= 22:  # Use self.working_days
            return salary * 10 / 100
        else:
            return 0
    
    def calculate_allowance(self):
        if self.position == 'GD':
            return 250000
        elif self.position == 'PGD':
            return 200000
        elif self.position == 'TP':
            return 180000
        elif self.position == 'NV':
            return 150000
        else:
            return 0
    
    def total_income(self):
        return self.calculate_salary() + self.calculate_bonus() + self.calculate_allowance()
    
    def __str__(self):
        return f'{self.ID} {self.name} {self.calculate_salary()} {self.calculate_bonus()} {self.calculate_allowance()} {self.total_income()}'

if __name__ == '__main__':
    ID = "NV01"
    name = input()
    base_salary = int(input())
    working_days = int(input())
    position = input()
    employee = Employee(ID, name, base_salary, working_days, position) 
    print(employee)
