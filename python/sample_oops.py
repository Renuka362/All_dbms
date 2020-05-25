class Employee:
    def __init__(self,first,last,pay):
        self.__first = first
        self.__last = last
        self.__pay = pay
        self.__email = first+last+'@gmial.com'
        