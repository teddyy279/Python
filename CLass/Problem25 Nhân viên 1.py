class Employee:
    def __init__(self, ID, name, gender, birth_of_date, address, TaxCode, signed_date):
        self.ID = str(ID)
        while len(self.ID) < 5:
            self.ID = '0' + self.ID
        self.name = name
        self.gender = gender
        self.birth_of_date = birth_of_date
        self.address = address
        self.TaxCode = TaxCode
        self.signed_date = signed_date
    
    def normalize_birth_of_date(self):
        if self.birth_of_date[1] == '/':
            self.birth_of_date = '0' + self.birth_of_date()
        if self.birth_of_date[4] == '/':
            self.birth_of_date = self.birth_of_date[0 : 3] + '0' + self.birth_of_date[3 :]

    def normalize_signed_date(self):
        if self.signed_date[1] == '/':
            self.signed_date = '0' + self.signed_date
        if self.signed_date[4] == '/':
            self.signed_date = self.signed_dateơ[0 : 3] + '0' + self.signed_date[3 :]

    def __str__(self):
        return f'{self.ID} {self.name} {self.gender} {self.birth_of_date} {self.address} {self.TaxCode} {self.signed_date}'
    

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        employee = Employee(i + 1, input(), input(), input(), input(), input(), input())
        employee.normalize_birth_of_date()
        employee.normalize_signed_date()
        a.append(employee)
    
    for x in a:
        print(x)
