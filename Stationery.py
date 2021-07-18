class Stationery:
    def draw(self):
        title = "Канцелярские принадлежности"
        print("Запуск отрисовки", title)

class Pen(Stationery):
    def draw(self):
        title = "ручка"
        print("Пишущая", title)

class Pencil(Stationery):
    def draw(self):
        title = "карандаш"
        print("Используем", title)

class Handle(Stationery):
    def draw(self):
        title = "маркер"
        print("Непишущий", title)

S = Stationery()
S.draw()

P = Pen()
P.draw()

Penc = Pencil()
Penc.draw()

H = Handle()
H.draw()
