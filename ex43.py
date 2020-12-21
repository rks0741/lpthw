from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    quips = [
    "You died. You kinda suck at this.",
    "Your momo would be proud...if she were smarter.",
    "Such a looser.",
    "I have a small puppy, that is better at this.",
    "You are worse than your dads jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        The Gothorns planet Percal have invaded your ship and
        destroyed the entire crew. you are the last surviver.
        you are running down the central corridor to weapons
        armory, when Gothon jumps out on you. He is blocking the way
        and about to blast you out
        """))

        action = input("what are you going to do? shoot, dodge, tell a joke> ")

        if action == "shoot":
            print(dedent("""
            montster eats you
            """))
            return 'death'

        elif action == "dodge":
            print(dedent("""
            you slips and monster eats you
            """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
            monster stars to laugh and you run past him
            """))
            return 'laser_weapon_armory'
        else:
            print ("DOES NOT COMPUTE!!!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        guess the codelock, 3 digits, 10 trys
        """))
    #    code = f"{randint(1,2)},{randint(1,2)},{randint(1,2)}"
        code = f"{int(1)},{int(2)},{int(1)}"
        print(code)
        guess = input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print("BUZZED!!!")
            guesses += 1
            guess = input ("[Keypad]> ")

        if guess == code:
            print(dedent("""
            you open the container
            you take the bomb and run to the TheBridge
            po place the bomb
            """))
            return 'the_bridge'
        else:
            print(dedent("""
            you have failed to
            open the lock, the bomb is sealed
            and aliens have blown your ship
            you died
            """))
            return 'death'


class TheBridge(Scene):
    def enter (self):
        print(dedent("""
        you burst into the bridge with the neutron destruct bomb
        and saw 5 Gothons, trying to take control over the ship.
        They have not pulled their weapons yet since they saw
        a bomb in your arms
        """))
        action = input("throw the bomb, slowly place the bomb >  ")
        if action == "throw the bomb":
            print(dedent("""
            You throw the bomb to the Gorthons
            but the shoot you in return
            """))
            return 'death'

        elif action == "slowly place the bomb":
            print(dedent("""
            you point your blaster on the bomb,
            aliens start ot sweat, you go backwards to the door.
            You seal the aliens and go to the escape pod
            """))
            return 'escape_pod'

        else:
            print("Does not compute!!")
            return 'the_bridge'


class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        You rush through the ship
        trying to reach escape pod before the ship is blown.
        It seems that there are no aliens on the ship, so
        you had no unexpected meeting during your trip.
        there are 5 pods, some may be damaged,
        which one wopuld you chose?
        """))
        good_pod = randint(1,1)
        guess = input("[pod #]>  ")
        if int(guess) != good_pod:
            print(dedent(f"""
            you jump into the pod {guess} and hit
            eject button. The pod escapes into the space. but then
            implodes, crushing your body into some red jelly
            """))
            return 'death'

        else:
            print(dedent(f"""
            You jump into the pod {guess}
            and hit the eject button. Pod easily slides out to the space,
            heading to the planet below. As it flies, you look back and
            see the ship implodes and the explodes, bright like a stars
            """))
            return 'finished'

class Finished (Scene):
    def enter(self):
        print("You won, good job!")
        return 'finished'

class Map(object):

    scenes = {'central_corridor':CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished(),
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map ('central_corridor')
a_game = Engine(a_map)
a_game.play()
