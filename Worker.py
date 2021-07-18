
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus};

class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)
    def get_total_income(self):
        print(sum(self._income.values()))

Some_worker = Position("Vladislav","Zakharenkov","CEO", 350000, 10000000)
Some_worker.get_full_name()
Some_worker.get_total_income()
