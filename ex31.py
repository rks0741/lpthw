print("""You enter a dark room with two doors.
Do you go through the door #1 or door  #2?""")

door = input("> ")

if door == "1":
    print("There is a guant bear here eating a cheescake!")
    print("What do you do?")
    print("1. Take the cake!")
    print("2. Scream at the bear!")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats yor legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably the best choise.")
        print("Bear runs away...")

elif door == "2":
    print("You are staring into the endless abyss at Ctulhu retina.")
    print("1. Bluberries.")
    print("2. Yellow jacket clothespins")
    print("3. Understanding revolvers yelling melodies")

    insanity = input("> ")
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello")
        print("Good job!")
    else:
        print("the insanity rots your eyes into the pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
