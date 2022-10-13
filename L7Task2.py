from abc import ABC, abstractmethod


class Clothes():

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @abstractmethod
    def result(self):
        pass

    def __str__(self):
        return str(self.width, self.height)


class Coat(Clothes):

    @property
    def result(self):
        return round(self.width / 6.5 + 0.5)


class Suit(Clothes):

    @property
    def result(self):
        return round(self.height * 2 + 0.3)


coat = Coat(46, 1.75)
suit = Suit(65, 1.65)

print(coat.result)
print(suit.result)
