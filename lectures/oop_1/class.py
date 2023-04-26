class Student:
    def __init__(self, name, netid, debt_amount, credits=0):
        self.name = name
        self.netid = netid
        self.debt_amount = debt_amount
        self.credits = credits

    def greet_person(self):
        print("Hello! My name is {}".format(self.name))

    def pay_down_debt(self, amount):
        self.debt_amount -= amount


sebastian = Student("Sebastian", "src402", 1.0)  # sebastian is an object of the Student class
sebastian.greet_person()

daniel = Student("Daniel", "dat9835", 5000.0)  # daniel is an object of the Student class
daniel.greet_person()
daniel.pay_down_debt(-500)
print(daniel.debt_amount)
