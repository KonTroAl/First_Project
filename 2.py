class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


val_1 = input("Enter number 1 - ")
val_2 = input("Enter  number 2 - ")

try:
    val_1 = int(val_1)
    val_2 = int(val_2)
    if val_2 == 0:
        raise OwnError("Делитель не должен быть равен 0!")
    result = val_1 / val_2
except OwnError as err:
    print(err)
except ValueError:
    print("Need a number!")
else:
    print(result)
