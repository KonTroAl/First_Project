class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


num = 0
b = []
while True:
    if input('Для выхода из программы введите "stop", для продолжения "Enter": ') == 'stop':
        break
    num += 1

    try:
        n = input("Введите число: ")
        if n.isdigit():
            b.append(n)
        else:
            raise OwnError("Enter number, please!")

    except OwnError as err:
        print(err)

    print(f"Your list:\n{b}")
