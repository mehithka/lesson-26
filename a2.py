class Person(object):
    def __init__ (self, name , idnumber):
        self.name = name 
        self.idnumber= idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class Employee(Person):
    def __init__ ( self, name, idnumber,salary, post):
        self.salary =  salary
        self.post = post

        Person.__init__(self,name,idnumber)

a = Employee('Rahul','811245861','500,000','Manager')

a.display()