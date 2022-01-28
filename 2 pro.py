class Car:
    def __init__(self, make, years_model):
        self.__make=make
        self.__years_model=years_model
        self.__speed=0
    def accelarate(self):
        self.__speed+=5
    def brake(self):
        self.__speed-=5
    def get_speed(self):
        return self.__speed
time_machine=Car('Delo', 'DCM-12 1981')
print('\033[4mTime (s)\033[0m   \033[4mSpeed (mph)\033[0m')
for i in range (5):
    time_machine.accelarate()
    speed=time_machine.get_speed()
    print(format(i + 1, '4d'), format(speed, '13d'))
for i in range(5):
    time_machine.brake()
    speed=time_machine.get_speed()
    print(format(i+6, '4d'), format(speed, '13d'))
