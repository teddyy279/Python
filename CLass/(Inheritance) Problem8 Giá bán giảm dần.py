class Vehicle:
    def __init__(self, ID, name, manufacturer, color, price):
        self.ID = ID
        self.name = name 
        self.manufacturer = manufacturer
        self.color = color
        self.price = price

    def get_price(self):
        return self.price

    def __str__(self):
        return self.ID + ' ' + self.name + ' ' + self.manufacturer + ' ' + self.color

class Motorcycle(Vehicle):
    def __init__(self, ID, name, manufacturer, color, price, max_speed):
        Vehicle.__init__(self, ID, name, manufacturer, color, price)
        self.max_speed = max_speed

    def get_ID(self):
        return self.ID

    def __str__(self):
        return Vehicle.__str__(self) + ' ' + str(self.max_speed) + ' ' + str(self.price)

class Car(Vehicle):
    def __init__(self, ID, name, manufacturer, color, price, horse_power):
        Vehicle.__init__(self, ID, name, manufacturer, color, price)
        self.horse_power = horse_power

    def get_ID(self):
        return self.ID

    def __str__(self):
        return Vehicle.__str__(self) + ' ' + str(self.horse_power) + ' ' + str(self.price)

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
            price = int(input())
            c = Car(ID, name, manufacturer, color, price, horse_power)
            car.append(c)
        else:
            name = input()
            manufacturer = input()
            color = input()
            max_speed = input()
            price = int(input())
            m = Motorcycle(ID, name, manufacturer, color, price, max_speed)
            motorcycle.append(m)
        
    print("DANH SACH OTO :")
    car.sort(key=lambda x: (-x.get_price(), x.ID))
    for x in car:
        print(x)
    print("DANH SACH XE MAY :")
    motorcycle.sort(key=lambda x: (-x.get_price(), x.ID))
    for x in motorcycle:
        print(x)
