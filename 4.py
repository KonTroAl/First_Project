class Storage:
    def __init__(self):
        self.numTech = {}

    @staticmethod
    def takeTech():
        # my_dict = self.numTech{"name": Tech.my_func(), "value": value}
        pass

        # print(self.numTech)

    def giveTech(self):
        pass


class Tech:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.list = []

    def my_func(self):
        return self.name, self.number

    def show(self):
        self.list.append(self.name)
        print(self.list)

class Printer(Tech):
    def __init__(self, name, number, series):
        super().__init__(name, number)
        self.series = series

    def my_func(self):
        return self.name, self.number

    # def income(self):
    #     self.list.append(self.name)
    #     return self.list


class Scan(Tech):
    def __init__(self, name, number, speed):
        super().__init__(name, number)
        self.speed = speed

    def my_func(self):
        return self.name, self.number


class Xerox(Tech):
    def __init__(self, name, number, value):
        super().__init__(name, number)
        self.value = value

    def my_func(self):
        return self.name, self.number


tech = Tech("Hp", 25)
tech_1 = Printer("HP", 25, 25)
tech_2 = Scan("MSI", 12, 25)
tech_3 = Xerox("Canon", 5, 25)
print(tech_1.my_func())
print(tech_2.my_func())
print(tech_3.my_func())
# tech_1.income()
tech.show()

Storage.takeTech()
