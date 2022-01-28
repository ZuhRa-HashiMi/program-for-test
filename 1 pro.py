class Pit:
    def __init__(self,name, animal_type, age):
        self.__name=name
        self.__animal_type=animal_type
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def set_animal_type(self,animal_type):
        self.__animal_type=animal_type
    def age(self,age):
        self.__age=age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
name=input('\nWhat is youe pit name?')
animal_type=input('\nWhat is the type of your pit?')
age=int(input('enter the age of your piy?'))
pit1= Pit(name,animal_type,age)
print('\nName',pit1.get_name())
print('\nAnimal type', pit1.get_animal_type())
print('\nAge', pit1.get_age())
#because of learning, I add comment

