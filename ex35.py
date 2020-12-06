from sys import exit

def gold_room():

    print("This room is full of gold! How much would you take?")
    choise = input("> ")
    if "0" or "1" in choise:
        how_much = int(choise)
    else:
        dead("Man, learn to type a number!")

    if how_much < 50:
            print("Nice, you  are not greedy, you win!")
            exit(0)
    else:
            dead("You greedy bastrd!!")

def bear_room():
    print("There is a bear in the room")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of the door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choise = input("take honey, taunt bear or open door?  ")
        if choise == "take honey":
            dead("The bear looks at you and slaps your face off")
        elif choise == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through now!")
            bear_moved = True
        elif choise == "taunt bear" and bear_moved:
            dead("The bear gets pissed and chew your leg off")
        elif choise == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what you mean")

def cthulhu_room():
    print("Here you see a great evil Cthulhu")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life of eat your head?")
    choise = input (" flee or head? >")

    if "flee" in choise:
        start()
    elif "head" in choise:
        dead ("Well. that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good job!")
    exit()

def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one would you take?")

    choise = input ("left or right? > ")

    if choise == "left":
        bear_room()
    elif choise == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room untill you starve(")
start()
