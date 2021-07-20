from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption




class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size > 36:
            self.__size = size
        else:
            print(f"Wrong size, try again")

    @property
    def fabric_consumption(self):
        return self.__size / 6.5 + 0.5

class Suit(Clothes):
    def __init__(self, height):
        super().__init__()
        self.__height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if 150 < height < 200:
            self.__height = height
        else:
            print(f"Wrong height, we sew for people from 150 to 200 sm height")

    @property
    def fabric_consumption(self):
        return (2 * self.__height/100) + 0.3

coat = Coat(int(input(f" Enter your size: ")))
suit = Suit(int(input(f" Enter your height: ")))
print(f"{round(coat.fabric_consumption)} meters for coat")
print(f"{round(suit.fabric_consumption)} meters for suit")

