class House:

    def __init__(self, name, q_floor):
        self.name = name
        self.q_floor = q_floor

    def __len__(self):
        return self.q_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.q_floor}"

    def go_to(self, new_floor):
        if new_floor == 0 or new_floor > self.q_floor:
            print('Нет такого этажа!')
            return
        for i in range(0, new_floor):
            print(i + 1)

    def __eq__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor == other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __lt__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor < other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __le__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor <= other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __gt__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor > other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __ge__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor >= other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            #  если other - является экземпляром класса House, сравниваем, возвращаем результат сравнения
            return self.q_floor != other.q_floor
        else:
            #  если нет, возвращаем False
            return False

    def __add__(self, value):
        if isinstance(value, int):
            #  если value - целое, увеличиваем этажность
            self.q_floor += value
            return self
        #  во всех остальных случаях возвращаем сам объект
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__


h1 = h1 + 10  # __add__
print(h1)

print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
