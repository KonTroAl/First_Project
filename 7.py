class CompNum:
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def __add__(self, other):
        return f"{self.number_1 + other.number_1} + {self.number_2 + other.number_2}i"

    def __mul__(self, other):
        return f"{self.number_1 * other.number_1 + other.number_1 * other.number_2} + {self.number_1 * other.number_2 + other.number_1 * self.number_2}i"

    def __str__(self):
        return


"""Вводится два числа: первое - действительная часть, второе - мнимая часть"""
val_1 = CompNum(25, 5)
val_2 = CompNum(45, -6)
print(val_1 + val_2)
print(val_1 * val_2)
