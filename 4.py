class Storage:

    @staticmethod
    def take():

        a = tech_1.my_list()
        b = tech_2.my_list()
        c = tech_3.my_list()
        my_dict_1 = {"position_1": a[0], "value": int(a[1])}
        my_dict.update(my_dict_1)
        my_dict.update(position_2=b[0], value_2=int(b[1]))
        my_dict.update(position_3=c[0], value_3=int(c[1]))

        print(my_dict)

    @staticmethod
    def give(org, name, number):
        dict = my_dict
        arg = 0
        if name == dict["position_1"] or name == dict["position_2"] or name == dict["position_3"]:
            arg = name
            if dict["value"] > 0 or dict["value_2"] > 0 or dict["value_3"] > 0:
                
                print(f"{name}, {number} in {org}")
            else:
                print(f"{name} not on sclad")
        else:
            print(f"Don't have such tech!")


class Tech:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.list = []

    def my_func(self):
        return self.name, self.number

    def my_list(self):
        self.list.append(self.name)
        self.list.append(self.number)
        return self.list


class Printer(Tech):
    def __init__(self, name, number, series):
        super().__init__(name, number)
        self.series = series


class Scan(Tech):
    def __init__(self, name, number, speed):
        super().__init__(name, number)
        self.speed = speed


class Xerox(Tech):
    def __init__(self, name, number, value):
        super().__init__(name, number)
        self.value = value


tech_1 = Printer("HP", 25, 25)
tech_2 = Scan("MSI", 12, 25)
tech_3 = Xerox("Canon", 5, 25)
# print(tech_1.my_func())
# print(tech_2.my_func())
# print(tech_3.my_func())
my_dict = {}

Storage.take()
Storage.give("OK", "popo", 5)
