# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, color, name=None, special=False):
        self._speed = 0
        self._color = color
        if name is None:
            self._name = "Абстрактная"
        else:
            self._name = name
        self._is_police = special

    def _prompt(self):
        print(self._name + " машинка" + ", " + self._color, end=", ")

    def go(self, speed):
        self._speed = speed
        self._prompt()
        print("разогналась до " + str(speed))

    def stop(self):
        self._speed = 0
        self._prompt()
        print("остановилась")

    def turn(self, direction):
        self._prompt()
        print("движется " + direction)

    def show_speed(self):
        self._prompt()
        print("движется со скоростью " + str(self._speed))


class TownCar(Car):
    def __init__(self, color):
        super().__init__(color, "Городская", False)

    def show_speed(self):
        super()._prompt()
        print("двигается со скоростью " + str(self._speed), end="")
        if self._speed > 60:
            print(". Превышение скорости")
        else:
            print("")


class WorkCar(Car):
    def __init__(self, color):
        super().__init__(color, "Рабочая", False)

    def show_speed(self):
        super()._prompt()
        print("двигается со скоростью " + str(self._speed), end="")
        if self._speed > 40:
            print(". Превышение скорости")
        else:
            print("")


class SportCar(Car):
    def __init__(self, color):
        super().__init__(color, "Спортивная", False)


class PoliceCar(Car):
    def __init__(self, color):
        super().__init__(color, "Полицейская", False)


print("Спортивная машина:")
a = SportCar("красная")
# К атрибутам можно было бы обратиться вот так: a.<имя  атрибута> = <значение>. Но это - дурной тон, и мы этого
# делать не будем, а сами атрибуты намеренно сделали защищенными
a.go(30)
a.go(50)
a.show_speed()
a.go(70)
a.show_speed()

print("Полицеская машина:")
b = PoliceCar("белая")
b.go(30)
b.go(50)
b.show_speed()
b.go(70)
b.show_speed()

print("Городская машина:")
c = TownCar("синяя")
c.go(30)
c.go(50)
c.show_speed()
c.go(70)
c.show_speed()

print("Рабочая машина:")
d = WorkCar("синяя")
d.go(30)
d.go(50)
d.show_speed()
d.go(70)
d.show_speed()
