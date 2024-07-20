##Polymorphism: more than one form
'''
----------
Human Being:
    in college student
    in theater audience
    in market customer
    in sports players
    in home child
 '''
'''
----------------------------------------------------------
RunTime:-Method Overriding
CompileTime:-Method Overloadng
----------------------------------------------------------
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f'{self.name},{self.age}'
class Student(Person):
    def __init__(self,name,age,roll,branch):
        super().__init__(name,age)
        self.roll=roll
        self.branch=branch
    def __str__(self):
        perdetails=super().__str__()
        return f'{perdetails},{self.roll},{self.branch}'

class Annualday(Student):
    def __init__(self,name,age,roll,branch,program):
        super().__init__(name,age,roll,branch)
        self.program=program
    def __str__(self):
        studetails=super().__str__()
        return f'{studetails},{self.program}'
#3
#aobj=Annualday('john',20,'68','cse','solo')
#print(aobj)

#2
#obj=Person('sanjana',555)
#print(obj)

#1
#obj=Student('sammy',6,111,'cse')
#print(obj)
