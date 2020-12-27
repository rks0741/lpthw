class Parent (object):
    def override(self):
        print("Parent override")

    def implicit(self):
        print("PAERENT IMPLICIT")

    def altered(self):
        print("PARENT altered")


class Child(Parent):
    def override(self):
        print("CHILD override")


    def altered(self):
        print("CHILD altered before PARENT")
        super(Child, self).altered()
        print("Child altered AFTER PARENT")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


#dad.altered()##
#son.altered()##
#dad.altered()##
#son.altered()##
#dad.altered()##
#son.altered()##
