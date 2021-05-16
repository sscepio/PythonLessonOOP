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



