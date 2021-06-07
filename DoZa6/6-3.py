# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий
# элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, f_name, l_name, pos, wage, bonus):
        self.name = f_name
        self.surname = l_name
        self.position = pos
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, f_name, l_name, pos, wage, bonus):
        super().__init__(f_name, l_name, pos, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["bonus"]


a = Position("John", "Doe", "Head of everything", 10000, 20000)
print(a.get_full_name() + " " + str(a.get_total_income()))
