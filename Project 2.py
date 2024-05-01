#Project 2: Hero vs. Monsters
import random

#Create monster-vulnerability dictionary:
Monsters = {"Dragon":"int_arrow","Zombie":"int_sword","Ghost":"int_magic","Minotaur":"int_hammer"}

def monster_game():
    heart_counter = 5
    print("Hello, and welcome to Hero vs. Monsters. You begin with 5 lives, each time you correctly defeat a monster you will face another. Otherwise, you will lose one of your lives. Let's begin!")
    while heart_counter > 0:
        generated_monst = random.choice(list(Monsters.keys()))
        int_arrow = 1
        int_sword = 2
        int_magic = 3
        int_hammer = 4

        if generated_monst == "Dragon":
            weapon = int(input("You are faced with a dragon! Select your weapon: "))
            if weapon == 1:
                print("You have successfully defeated the dragon!! Onto the next battle.")
            else:
                print("Wrong weapon selection- the dragon has cost you one of your hearts.")
                heart_counter -= 1
        elif generated_monst == "Zombie":
            weapon = int(input("You are faced with a zombie! Select your weapon: "))
            if weapon == 2:
                print("You have successfully defeated the zombie!! Onto the next battle.")
            else:
                print("Wrong weapon selection- the zombie has cost you one of your hearts.")
                heart_counter -= 1
        elif generated_monst == "Ghost":
            weapon = int(input("You are faced with a ghost! Select your weapon: "))
            if weapon == 3:
                print("You have successfully defeated the ghost!! Onto the next battle.")
            else:
                print("Wrong weapon selection- the ghost has cost you one of your hearts.")
                heart_counter -= 1
        else:
            weapon = int(input("You are faced with a minotaur! Select your weapon: "))
            if weapon == 3:
                print("You have successfully defeated the minotaur!! Onto the next battle.")
            else:
                print("Wrong weapon selection- the minotaur has cost you one of your hearts.")
                heart_counter -= 1
    else:
        print("You have lost all of your lives. Good game!")
        #choice = input("You have lost your last heart. Would you like to restart? (yes/no):")

print(monster_game())
