class Other (object):
    def override(self):
        print("Other override")

    def implicit(self):
        print("Other implicit")

    def altered(self):
        print("Other altered")


class Child(Other):

    def __init__(self):
        self.other = Other()
        print("Initiated")

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override")


    def altered(self):
        print("CHILD altered before other")
        self.other.altered()
        print("Child altered AFTER other")



son = Child()
print("After initiation we run scripts")
son.implicit()
son.override()
son.altered()
