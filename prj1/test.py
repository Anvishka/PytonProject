from random import *

class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to Study! ;(")
        self.progress += 0.12
        self.gladness -= 3


    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):

        if self.progress < -0.5:
            print("Cast out")
            self.alive = False

        elif self.gladness <= 0:
            print("Dapression")
            self.alive = False

        elif self.progress > 5:
            print("Passed externally")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")

    def live(self,day):
        print(f"Day - {day} of {self.name}  ")

        live_cube = randint(1,3)

        if live_cube == 1:
            self.to_study()

        elif live_cube == 2:
            self.to_chill()

        elif live_cube == 3:
            self.to_sleep()

        self.end_of_day()

        self.is_alive()

Artem = Student("Artem")


for day in range(365):

    if Artem.alive == False:
        break

    Artem.live(day)
