## Animal is-a object (yes, confusing) look at the extra credit

class Animal(object):
    def walk(self):
        print("I am walking!")

## Dog is-a Animal class

class Dog(Animal):
    def __init__(self, name):
        ## Dof has-a name
        self.name = name

## Cat is a animal class
class Cat(Animal):
    def __init__(self, name):
        ##cat has a name
        self.name = name


## Person is an object
class Person(object):
    def __init__(self, name):
        self.name = name

        ##Person has a pet of some kind
        self.pet = None

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ##
        super(Employee, self).__init__(name)
## employee has a salary
        self.salary = salary
##Fish is an object
class Fish(object):
    ## fish has a name
    def __init__(self, name):
        self.name = name
    ##fish can swim
    def swim(self):
        print(self.name, " ", " is swimming!")
## salmon is a Fish
class Salmon(Fish):
    pass

#Halibutu is a Fish

class Halibut(Fish):
    pass

    #rover is a Dog
rover = Dog("Rover")
rover.walk()
#Satan is a Cat
satan = Cat("Satan")
#Mary is a Person
mary = Person("Mary")
#mary has a pet Satan
mary.pet = satan
#frank is a person and Employee
frank = Employee("Frank", 120000)
#Frank has a pet Rover
frank.pet = rover
#Flipper is a Fish
flipper = Fish("Flipper")
flipper.swim()
crouse = Salmon("Crouse")

harry = Halibut("Harry")
