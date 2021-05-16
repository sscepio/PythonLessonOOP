# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу
# можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
# завершать скрипт.

class TrafficLight:
    __color = "красный"
    def running (self, end):

       while end < 12:
            if end <= 7:
              self.color = "красный"
            elif end >= 8 and end <= 9:
              self.color = "желтый"
            elif end >= 9 and end <= 12:
                self.color = "зеленый"
            return self.color

traffic = TrafficLight()
for i in range(0, 12, 1):
    print(f"Сейчас светофор: {traffic.running(i)}")
# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения
# данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод
# расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина *
# масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода. Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _lenght = 0
    _width = 0
    def __init__(self, lenght, width):
            self._width = width
            self._lenght = lenght
    def calculate(self):
        print(f"Масса асфальта равна {self._lenght * self._width * 25 * 0.5 / 1000} ТОНН")
road = Road(20, 5000)
road.calculate()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (
# должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (
# get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).
income = {}
class Worker:
    name = ""
    surname = ""
    position = ""
    wage = 0
    bonus = 0
    _income = income
    def __init__(self, name, surname, position, wage, bonus):
         self._name = name
         self._surname = surname
         self._position = position
         self._wage = wage
         self._bonus = bonus
         self._income[f"bonus{name}{surname}"] = bonus
         self._income[f"wage{name}{surname}"] = wage
    def workerInfo(self):
        print(f'Имя {self._name} Фамилия {self._surname} Должность {self._position}', self._income[f"wage{self._name}{self._surname}"], self._income[f"bonus{self._name}{self._surname}"])
worker = Worker ("Гарегин", "Папян", "Директор клиента", 120000, 20000)
print(worker.workerInfo())
print(income)
class Position(Worker):
    def getFullName(self):
        print(self._name)


position = Position("Гарегин", "Папян", "Директор клиента", 150000, 10000)
position.getFullName()
position.workerInfo()

# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (
# булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar
# переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
# сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stationery:
    _title = ""
    def __init__(self, title):
        self.title = title
    def draw (self):
        print("Запуск отрисовки")
class Pencil (Stationery):
    def draw(self):
        print("Рисую...")
class Handle (Stationery):
    def draw(self):
        print("Маркерую...")
class Pen (Stationery):
    def draw(self):
        print("Пишу...")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
pen.draw()
pencil.draw()
handle.draw()
