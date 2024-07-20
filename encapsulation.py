'''
##Encapsulation:-
                Binding or wraping up the data and methods into the single component is called
                encapsulation.
            ##EXAMPLE:-
                  class is the best example of encapsulation
            ##ADVANTAGES:-
                      *)Code integration:
                      security

                      *)Access modifiers:
                         public,private,protected
    '''
##Example:-
class Employee:
    def __init__(self,name,role,salary):
        self.name=name
        self.role=role
        self.__salary=salary         #private method

    def get_salary(self):             #public method and data is private data
        print(self.__salary)        
    
    def Empdisplay(self):            # public method
        print(self.name,self.role)
        
class Company(Employee):
    def __init__(self,cname,loc):
       self.cname=cname
       self.loc=loc
    
    def Comdisplay(self):
        print(self.cname,self.loc)
    def _hiring(self):         #protected method
        print('Hiring For The Manager Role')
        
        
cobj=Company('Infosys','HiTechCity')
eobj=Employee('Sanjana','Gouthami',900000)
eobj.Empdisplay()
print(cobj._hiring())


        
