class Customer:
    def __init__(self, username, password, name, entry_time, exit_time):
        self.username = username
        self.password = password
        self.name = name
        self.entry_time = entry_time
        self.exit_time = exit_time
    
    def calculate_play_time(self):
        entry_hour, entry_minute = int(self.entry_time[:2]), int(self.entry_time[3 : 5])
        exit_hour, exit_minute = int(self.exit_time[:2]), int(self.exit_time[3 : 5])
        return (exit_hour * 60) + exit_minute - (entry_hour * 60) - entry_minute

    def solveTime(self):
        res = ""
        res += str(self.calculate_play_time() // 60)
        res += "gio"
        res += str(self.calculate_play_time() % 60)
        res += "phut"
        return res

    def __str__(self):
        return f'{self.username} {self.password} {self.name} {self.solveTime()}'

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        customer = Customer(input(), input(), input(), input(), input())
        a.append(customer)
    
    a.sort(key = lambda x : -x.calculate_play_time())
    for x in a:
        print(x)
