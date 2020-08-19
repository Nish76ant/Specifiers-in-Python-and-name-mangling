"""
Public
Private
Protected
"""

class Employee:

    noOfLeaves = 8
    var = 8
    _protech = 5
    __private = 98


    def __init__(self,name,role,salary):
           self.name = name
           self.role = role
           self.salary = salary

    def printDetailsofEmp(self):
        return f'Hey your name is {self.name} and your role  is {self.role} and your salary is {self.salary}'

    @classmethod
    def changeOfleaves(cls,newleaves):
           cls.noOfLeaves = newleaves 

    @classmethod
    def from_str(cls,string):
        params = string.split("-")
        #print(params)
        return cls(params[0],params[1],params[2])
    
    @staticmethod
    def printgood(string):
        print('This is good'+string)  
        return 'Hii' 

harry = Employee('Harry','Programmar',141)
print(harry._protech)
print(harry._Employee__private)
#print(harry.__private) ,give the error #name mangling in Python


