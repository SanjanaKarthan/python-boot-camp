##python is rich for libries and modules
'''
##ABSTRACTION:-
              hiding the internal data(ABSTRACT METHOD)
              abstract class contains abstract and non abstract
              other name of non abstract is concrete method(if we are writing body then it is non abstract)
              abstract class doesnot have body
--------------------------------------------------------------------------
'''
##Abstract
'''Example-1
from abc import ABC


class RBIBANK(ABC):
    def interest(self):
        pass
    def loan(self):
        print("provides home loans")#CONCRETE METHOD
class HDFC(RBIBANK):
    def interest(self):
        print("7.5% interest")
class SBI(RBIBANK):
    def interest(self):
        print("11% interest")
class AXIS(RBIBANK):
    def interest(Self):
        print("9% interest")
h1=HDFC()
h1.loan()
h1.interest()
s1=SBI()
s1.loan()
s1.interest()
a1=AXIS()
a1.loan()
a1.interest()
------------------------------------------------------------------------------------
'''
'''Example-2
from abc import ABC

class Vehicle(ABC):
    def speed():
        pass
    def milage():
        pass
    def model():
        pass
    def breaks():
        print('stop the vehicle')
        
class RangeRover(Vehicle):
    def speed():
        print('450 max speed')
    def milage():
        print('12KMPH')
    def model():
        print('new  model')

class Porche(Vehicle):
    def speed():
        print('850 max speed')
    def milage():
        print('15KMPH')
    def model():
        print('new  model')
fobj=RangeRover
fobj.milage()
fobj.speed()
fobj.model()
fobj.breaks()
fobj1=Porche
fobj1.milage()
fobj1.speed()
fobj1.model()
fobj1.breaks()
'''       



    
