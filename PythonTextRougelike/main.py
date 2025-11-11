import os
import random
import time
import battlesystem
twand = False
fwand = False
iwand = False
paralysis_spell = False
poison_spell = False
death = 0
upgrade_counter = 0
health = 10
begin = 0
def cls():
    os.system("clear")
def main():
    print("________                                                 ________                          __ ")  
    print("\______ \  __ __  ____    ____   ____  ____   ____       \_____  \  __ __   ____   _______/  |_ ")
    print(" |    |  \|  |  \/    \  / ___\_/ __ \/  _ \ /    \       /  / \  \|  |  \_/ __ \ /  ___/\   __\ ")
    print(" |    `   \  |  /   |  \/ /_/  >  ___(  <_> )   |  \     /   \_/.  \  |  /\  ___/ \___ \  |  |  ")
    print("/_______  /____/|___|  /\___  / \___  >____/|___|  /     \_____\ \_/____/  \___  >____  > |__|  ")
    print("        \/           \//_____/      \/           \/             \__>           \/     \/      ")
    print()
    print("WELCOME TO DUNGEON QUEST! ")
    print()
    while True:
        start = input("Press ENTER to start. Enter 'help' to get to the help menu. ")
        if start == "":
            begin = 1
            cls()
            while True:
                start2 = input("Press ENTER to fight an enemy. ")
                if start2 == "":
                    while death == 0:
                        battlesystem.battle()
                    cls()
        elif start == "help": 
            print()
            print("Welcome to EncounterTest! This is atext based game I am working on.")
            print("Upon starting the game, press enter to get into a fight")
            print("There are quite a few enemies in this game, and in the future I will add more.")
            print("You will have the option to attack or use magic. ")
            print("You will be able to see the stats of both of these.")
            print("Every five floors, you will have the option to upgrade your max health.")
            print()
            lmao = input("Press enter to leave.")
            cls()
            main()
            
main()