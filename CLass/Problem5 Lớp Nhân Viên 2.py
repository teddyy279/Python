class Employee:
    def __init__(self, ID, name, gender, date_of_birth, address, TaxCode, signed_date):
        self.ID = ID
        self.name = name
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.address = address
        self.TaxCode = TaxCode
        self.signed_date = signed_date
    def normalize(self):
        if self.date_of_birth[1] == '/':
            self.date_of_birth = '0' + self.date_of_birth 
        if self.date_of_birth[4] == '/':
            self.date_of_birth = self.date_of_birth[0 : 3] + '0' + self.date_of_birth[3:]
        if signed_date[1] == '/':
            self.signed_date = '0' + self.signed_date
        if signed_date[4] == '/':
            self.signed_date = self.signed_date[0 : 3] + '0' + self.signed_date[3 :]
    def __str__(self):
        return f'{self.ID} {self.name} {self.gender} {self.date_of_birth} {self.address} {self.TaxCode} {self.signed_date}'

if __name__ == '__main__':
    name = input()
    gender = input()
    date_of_birth = input()
    address = input()
    TaxCode = input()
    signed_date = input()
    Employee = Employee("00001", name, gender, date_of_birth, address, TaxCode, signed_date)
    Employee.normalize()
    print(Employee)
