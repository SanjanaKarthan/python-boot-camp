'''
###INHERITANCE:-types of inheritance
1)single
2)multiple
3)multi level
4)hierarical
5)hybrid
'''
##single inheritance
'''
class jntu:
    def schedule_academics(self):
        print('scheduling academics')
    def declare_holidays(self):
        print('national and summer holidays')
    def results(self):
        print('go to www.jntuhresults.com')
class SriDevi(jntu):
    def fees(self):
        print('3rd year fee is 85k')
jobj=jntu()
jobj.results()
#jobj.fees()
s1=SriDevi()
s1.schedule_academics()
s1.declare_holidays()
-----------------------------------------------
##multiple inheritance:-
                       one child class deriving from the two parent classes
                        multiple inheritance is not possible in java
-------------------------------------------------------------------

