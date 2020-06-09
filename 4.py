class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Storage:

    @staticmethod
    def take():
        a = tech_1.my_list()
        b = tech_2.my_list()
        c = tech_3.my_list()
        my_dict_1 = {a[0]: int(a[1])}
        my_dict.update(my_dict_1)
        my_dict_1 = {b[0]: int(b[1])}
        my_dict.update(my_dict_1)
        my_dict_1 = {c[0]: int(c[1])}
        my_dict.update(my_dict_1)
        print(f"On sclad:\n{my_dict}")

    @staticmethod
    def give(org, name, number):
        try:
            dict = list(my_dict.keys())
            val = list(my_dict.values())
            if name == dict[0] or name == dict[1] or name == dict[2]:
                if val[0] > 0 or val[1] > 0 or val[2] > 0:
                    number = int(number)
                    if number < 0:
                        raise OwnError(f"{number} - need to be positive!")
                    result = my_dict[name] - number
                    if result >= 0:
                        my_dict[name] = result
                        print(f"{name}, {number} in {org}")
                        print(my_dict)
                    else:
                        print(f"You want too much!\nOn sclad:\n{my_dict}")
                else:
                    print(f"{name} not on sclad")
            else:
                print(f"We don't have tech like this: {name}")
        except ValueError:
            print(f"Incorrect {number}! Enter positive number!")
        except OwnError as err:
            print(err)


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

my_dict = {}

Storage.take()
Storage.give("OK", "HP", 5)
Storage.give("OK", "MSI", 5)
