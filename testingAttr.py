

# class Student:
#
#     def __init__(self,name,score):
#         self.__name = name
#         self.__score = score
#
#     def print_attr(self):
#         print('%s -- %s' %(self.__name,self.__score))
#
#     def get_grade(self):
#         if self.__score >= 90:
#             return 'A'
#         elif self.__score >= 80:
#             return 'B'
#         else:
#             return 'c'
#
#     def get_name(self):
#         return self.__name
#     # def set_name(self,name):
#     #     self.__name = name
#
# bart = Student('lilie',90)
# # print(bart.__name)
# print('222',bart.get_name())
# print(bart.get_grade())



class Student:

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score mut be in integer")
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

s = Student()
s.score = 60
sc = s.score
print(sc)

class Runnable(object):
    def run(self):
        print('runing')

class Flyable(object):
    def fly(self):
        print('fly...')

class Dog(Runnable,Flyable):
    pass

dog = Dog()
dog.run()
dog.fly()