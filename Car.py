class Car:
    def __init__(self, speed, color, name, is_police: bool):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police
    def show_speed(self, current_speed):
        print("Текущая скорость", current_speed)
    def go(self):
        print("Автомобиль едет")
    def stop(self):
        print("Автомобиль остановился")
    def turn(self, direction):
        print("Автомобиль повернулл", direction)

class TownCar(Car):
    def spid_limit(self):
        if self.speed > 60:
            print("Вы превысили скорость, срочно остановитесь")

class WorkCar(Car):
    def spid_limit(self):
        if self.speed > 40:
            print("Вы превысили скорость, срочно остановитесь")

class PoliceCar(Car):
    def warning(self):
        print("Срочно остановитесь!")
class SportCar(Car):
    def speedtrap(self, topspeed):
        print("Вы пересекли отметку со скоростью", topspeed)
    def stats(self):
        print(f"Машина {self.name}, Максимальная скорость {self.speed}, Цвет {self.color}")

new_car = WorkCar("54", "red", "Zhuk", False)
new_car.show_speed(55)
new_car.turn("налево")
new_car.spid_limit()
print("/"*10)
new_car2 = PoliceCar(120, "Black", "Volvo", True)
print(new_car2.is_police)
new_car2.warning()
print("/"*10)
new_car3 = SportCar(400, "Red", "Ferrari", False)
new_car3.stats()
new_car3.speedtrap(398)




