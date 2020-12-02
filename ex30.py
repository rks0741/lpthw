people = 40
cars = 40
trucks = 55


if cars > people:
    print("We should take the cars")
elif cars< people:
    print("We should not take the cars")
else:
    print("we cant decide.")

if trucks > cars:
    print ("There are too many trucks!")
elif trucks < cars:
    print("Maybe we should take the trucks")
else:
    print("We still cant decide")

if people > trucks:
    print("Alright, lets just take the trucks")

else:
    print("Fine, lets stay home then")
