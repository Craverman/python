class Road:

    def __init__(self, length, width):
        self._lenght = length
        self._width = width
        print(f"{self._lenght}м * {self._width}м * 25кг * 5см =", self._lenght*self._width*25*5)

some_road = Road(31, 62)
