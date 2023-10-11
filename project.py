#variables
name = "jose"
last_name = "morales"
age = 22

#class
class Human():

    def __init__(self,p,q,r):
        self.name = p
        self.last_name = q
        self.age = r

    def weeding(self):
        print(f'My name is {self.name} {self.last_name} , I am {self.age} years old')

#object
me = Human(name,last_name,age)
me.weeding()

# changing properties
me.name = "JOSE FRANCISCO"
me.last_name = "MORALES CAQUI"
me.weeding()
