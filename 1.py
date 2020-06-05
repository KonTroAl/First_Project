class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def my_func(cls, param):
        el_1 = list(Data(param).data)
        A = [i for i in el_1 if i != "-"]
        B = [int(A[el - 1] + A[el]) for el in range(1, len(A), 2)]
        return B

    @staticmethod
    def valid(data_2):
        b = Data.my_func(data_2)
        if 1 <= b[1] <= 12 and 1 <= b[0] <= 31:
            print("Alright!")
        else:
            print("Incorrect data!")

    def func(self):
        return self.data


data_1 = Data("01-12-22")
Data.valid("01-12-22")

