import sys
from enum import Enum

# Global variables ============================================================

character = None

# Class defenitions ===========================================================

class Item(Enum):
    TORCH = 0

class Player:

    # constructor
    def __init__(self, name, hp, atk, res):
        # the name that the player inputs at the beginning of the game
        self.name = name
        # the maximum value for hit points
        self.mhp = hp
        # the actual value for hit points. If it drops below 0, the player dies
        self.hp = hp
        # the attack power of the player. Higher values results in attacks
        # that harm thier targets more
        self.atk = atk
        # the resillience power of the player. Higher values results in attacks
        # harming the player less
        self.res = res
        # the list that will contain all the items that the player has
        self.items = []
        # the experience points of the player
        self.exp = 0
        # the level of the player
        self.level = 1

    # displays all the information about the player.  If the argument passed
    # is True, then it will show items.  If not, items are not shown
    def display_info(self, items=True):
        print("Your are " +self.name+ ", a " +str(self.level)+ "adventurer.",
            "Your stats are: ")
        print("MaxHP: ", str(self.mhp))
        print("ATK:  ", str(self.atk))
        print("RES:  ", str(self.res))
        if items:
            print("You are currently carrying: ")
            for item in self.items:
                print(item.name)
            if len(self.items) == 0:
                print("Nothing")
        print("You currently have", str(self.hp), "out of", str(self.mhp),
            "hit points.")

    # gives the player's hp in the form of a string "x out of y"
    def current_hp:
        return str(self.hp) + " out of " + str(self.mhp)

    # check if the player has a certain Item
    def has_item(self, item):
        for i in items:
            if i == item:
                return True
        return False

    def attack(target):
        print("You attack the " + target.name)
        target.take_damage(atk)

    # method to take damage
    def take_damage(damage):
        dmg = max(damage - res, 0)
        print("You take " + str(dmg) + " damage!")
        hp -= dmg
        if is_dead():
            print("You have died")
            sys.exit()

    # checks if the player is dead.  If so, exit the game
    def is_dead():
        return hp <= 0

    # returns all the actions that the player can take in battle, as strings
    def battle_actions():
        ret = ["attack"]
        return ret

class Enemy:

    # constructor
    def __init__(self, name, hp, atk, res, exp):
        self.name = name
        self.mhp = hp
        self.hp = hp
        self.atk = atk
        self.res = res
        self.exp = exp

    def current_hp():
        return str(self.hp) + " out of " + str(self.mhp)

    def attack(target):
        print("The " + name + " attacks!")
        target.take_damage(atk)

    # death checking must be done seperately
    def take_damage(damage):
        dmg = max(damage - res, 0)
        print("The " + name + " takes " + dmg + " damage!")
        hp -= dmg

    def is_dead():
        return hp <= 0

# Methods handling player input ===============================================

# if the player gives an answer whose behavior does not depend on the location,
# this method handles it.  If not, it returns the players answer.  The argument
# should be a list of all valid answers with behavoir dependant on location
def get_player_answer(valid_answers):
    ans = None
    ans = input().lower()
    print()
    while ans not in valid_answers:
        if ans == "i":
            character.display_info()
        elif ans == "c":
            print("You can currently: ")
            for possibility in valid_answers:
                print(possibility)
            print("You can also type 'i' for info about your character, or",
            "'e' to exit the game.")
        elif ans == "e":
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid Answer. Try Again:")
        ans = input().lower()
        print()
    return ans

# this method just waits for the player to hit enter
def wait_for_enter():
    input()

# Methods handling different scenes ===========================================

# handles the scene where the player makes thier character.  Default commands
# like "i" anc "c" are disabled here
def character_creation():
    name = input("Type your name here:  ")
    hp = 20
    atk = 4
    res = 4
    print("Welcome ", name, "!")
    print("There are three stats in this game. Your Hit Points (HP) represent",
        "how many attacks you can take before you die.  Your Attack (ATK)",
        "represents how powerful your own attacks are, and your Resillience",
        "(RES) reduces the power of attacks that enemies make against you.")
    print()
    # choosing a strength
    print("Choose a strength:")
    print("1. HP")
    print("2. ATK")
    print("3. RES")
    answer = input()
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("Invalid Answer.  Choose a strength:\n")
    if answer == "1":
        hp += 5
    elif answer == "2":
        atk += 1
    elif answer == "3":
        res += 1
    print()
    # choosing a weakness
    print ("Now Choose a weakness. If you choose the same stat as your",
        "strength, you will have no weakness, but also no strength.")
    print("1. HP")
    print("2. ATK")
    print("3. RES")
    answer = input()
    while answer != "1" and answer != "2" and answer != "3":
        answer = input("Invalid Answer.  Choose a weakness:\n")
    if answer == "1":
        hp -= 5
    elif answer == "2":
        atk -= 1
    elif answer == "3":
        res -= 1
    # displaying character information
    global character
    character = Player(name, hp, atk, res)
    print()
    character.display_info(False)

# The entrance room to the dungeon
def entrance_room():
    print("You find youself in a dark, dank, dungeon. There's a door in front",
        "of you, leading North (At any time, press 'c' for the controls, 'i'",
        "for information about yourself, and 'x' to exit the game).")
    # there's only one possible answer, so an if isn't required
    get_player_answer(["open door"])
    first_crossroads()

# the crossroad right after the entrance.  The hallway to the left ins't
# accessible until you obtain a torch
def first_crossroads():
    print("You're now in a similarly dank room, with a door leading South,",
        "and two hallways going East and West. The one to the East is quite",
        "dark.")
    while False:
        ans = get_player_answer(["open door","go south","go east","go west"])
        # go south, go back to the entrance room
        if ans == "open door" or ans == "go south":
            entrance_room()
        # try to go east, but check if they have a torch
        if ans == "go east":
            if character.has_item(Item.TORCH):

                # go to the next room

            else:
                print("It's too dark to go east.")
        if ans == "go west":

            # go to the next room

# the room to the west of the first room.  It contains a goblin
def goblin_room():
    print("You walk into a small, well-lit room. In it stands a goblin.")
    goblin = Enemy("goblin", 8, 6, 1, 1)
    battle()

def battle(enemy):
    global character
    print("FIGHT\n")
    print("You've encountered a " + str(enemy.name) + "!  Your HP is" +
        character.current_hp)
    print("The " + str(enemy.name) + " has " + enemy.current_hp)
    while True:
        # get the player action
        print("You can: ")
        for i in character.battle_actions():
            print(i)
        ans = get_player_answer(character.battle_actions())
        # all the actions are checked for, but actions unlearned are prevented
        # by get_player_answer
        if ans == "attack":
            player.attack(enemy)
            if enemy.is_dead():
                break
        






def main():
    character_creation()
    entrance_room()


main()
