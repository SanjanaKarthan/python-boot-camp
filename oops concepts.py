'''
##OOPS:-Real time problems can be solved using oops

####CLASS:-structure of a object,blue print,logical entity
           class is a blue print of a object
           class is alogical entity
           class contains functions,construtor,data
SYNTAX:-
class class_name

---------------------------------------------------------------------------
####OBJECT:-behaviour,properties,
            object is real world entity
             object is a instanmce of a class
             OBJECT IS A SUB CLASS OF A CLASS
            objects contains properties,behaviour,identity
---------------------------------------------------------------------------------
###CONSTRUCTOR:-
     it is a special function or special method which is used to
     invoked instance variable(object variable) constructor doesnot return any value
    while creating the object constructor will call implicitly(automatically)
    there are three types of constructors:-1)default
                                           2)parameterized
                                           3)non parameterize

class Employee:
    def __init__(self,name,number,designation,address,email):
        self.name=name
        self.number=number
        self.designation=designation
        self.address=address
        self.email=email
    def display(self):
       print("Name is:",self.name)
       print("Number is:",self.number)
       print("Designation is:",self.designation)
       print("Address is:",self.address)
       print("Email is:",self.email)

s1=Employee('sanjana',7945205628,'Hr','Nagpur','sanjana@123gmail.com')
s1.display()
'''
'''
-----------------
###static data:-
               STATIC IS USED FOR MEMORY MANAGEMENT(IT IS USED FOR MEMEORY CONSUMPTION)
##instead of creating individually, a common data create a
static data ans pass the copy to allthe objects.
'''
'''
class student:
    branch='cse'
    def __init__(self,name,roll,address,phonenum,email):
        self.name=name
        self.roll=roll
        self.address=address
        self.phonenum=phonenum
        self.email=email
    def display(self):
       print("Name is:",self.name)
       print("Roll is:",self.roll)
       print("Branch is:",branch)
       print("Address is:",self.address)
       print("Phone num is:",phonenum)
       print("Email is:",self.email)
       print()

s1=student('sanjana','496','Nagpur','sanjana@123gmail.com')
s2=student('goutham','567','hyderbad','gounan@gmail.com')
s1.display()
s2.display()

'''       

####without using display####
class student:
    branch='cse'
    def __init__(self,name,number,roll,address,email):
        self.name=name
        self.number=number
        self.roll=roll
        self.address=address
        self.email=email
    def __str__(self):
        return f'{self.name} {self.number} {self.roll} {student.branch} {self.address} {self.email}'
s1=student('sanjana',7945205628,596,'Nagpur','sanjana@123gmail.com')
s2=student('goutham',856372578,678,'hyderbad','dahkiyu@gmail.com')
print(s1)
print(s2)

'''
------------------------------------------------------------------------------------
abstraction                               
encapsulation
inhertiance
polymorphism
'''
