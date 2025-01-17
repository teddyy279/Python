class Vehicle:
    def __init__(self, ID, name, manufacturer, color, price):
        self.ID = ID
        self.name = name 
        self.manufacturer = manufacturer
        self.color = color
        self.price = price

    def __str__(self):
        return self.ID + ' ' + self.name + ' ' + self.manufacturer + ' ' + self.color

class Motorcycle(Vehicle):
    def __init__(self, ID, name, manufacturer, color, price, max_speed):
        Vehicle.__init__(self, ID, name, manufacturer, color, price)
        self.max_speed = max_speed

    def get_manufacturer(self):
        return self.manufacturer

    def __str__(self):
        return Vehicle.__str__(self) + ' ' + self.max_speed + ' ' + str(self.price)

class Car(Vehicle):
    def __init__(self, ID, name, manufacturer, color, price, horse_power):
        Vehicle.__init__(self, ID, name, manufacturer, color, price)
        self.horse_power = horse_power

    def get_manufacturer(self):
        return self.manufacturer

    def __str__(self):
        return Vehicle.__str__(self) + ' ' + self.horse_power + ' ' + str(self.price)

if __name__ == '__main__':
    n = int(input())
    motorcycle, car = [], []
    for _ in range(n):
        ID = input()
        if ID[:3] == "OTO":
            name = input()
            manufacturer = input()
            color = input()
            horse_power = input()
            price = input()
            c = Car(ID, name, manufacturer, color, price, horse_power)
            car.append(c)
        else:
            name = input()
            manufacturer = input()
            color = input()
            max_speed = input()
            price = input()
            m = Motorcycle(ID, name, manufacturer, color, price, max_speed)
            motorcycle.append(m)
        
    manufacturer = input()    
    print("DANH SACH XE HANG " + manufacturer + ' :')
    for x in car:
        if(x.get_manufacturer() == manufacturer):
            print(x)
    for x in motorcycle:
        if(x.get_manufacturer() == manufacturer):
            print(x)
