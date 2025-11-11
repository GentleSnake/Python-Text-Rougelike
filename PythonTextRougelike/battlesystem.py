import os
import random          #Imports all of the nescesary stuff for it
import time         #To function
global enemy
from random import choice
def cls():
    os.system('clear')  # teaches the system how to clear the console
health = 10
max_health = 10
upgrade_counter = 1
upgrade_counter_min = 1
dmg = 3
magic_damage = 5
goldmax = 0
enemy = 0
inventory = []
enemy_list = ["GEBLIN", "ZORBO", "HAIRIMP", "BATTRAX", "WARRACK","GHOSTWOOD","BOMBLOONS","TRICKSTER GOD DREVA"]


def battle():
    global health
    global enemy_health
    global max_health
    global upgrade_counter
    global death
    global upgrade_choice
    global dmg
    global magic_damage
    global goldmax
    enemy_found = choice(enemy_list)    #Picks random enemy
    if enemy_found == "BATTRAX":            #And asigns them different stats
        enemy = "BATTRAX"
        enemy_health = 9
        gold = 30
        enemydmg = 4
    elif enemy_found == "GEBLIN":
        enemy = "GEBLIN"
        enemy_health = 5
        gold = 40
        enemydmg = 3
    elif enemy_found == "WARRACK":
        enemy = "WARRACK"
        enemy_health = 7
        gold = 50
        enemydmg = 3
    elif enemy_found == "ZORBO":
        enemy = "ZORBO"
        enemy_health = 1
        gold = 10
        enemydmg = 2
    elif enemy_found == "HAIRIMP":
        enemy = 'HAIRIMP'
        enemy_health = 2
        gold = 40
        enemydmg = 3
    elif enemy_found == "GHOSTWOOD":
        enemy = "GHOSTWOOD"
        enemy_health = 7
        gold = 60
        enemydmg = 6
    elif enemy_found == "BULLTROLL":
        enemy = "BULLTROLL"
        enemy_health = 11
        gold = 100
        enemydmg = 5
    elif enemy_found == "BOMBLOONS":
        enemy = "BOMBLOONS"
        enemy_health = 2
        gold = 15
        enemydmg = 3
    if upgrade_counter == "TRICKSTER GOD DREVA":
        enemy = "THE TRICKSTER GOD DREVA"
        enemy_health = 25
        gold = 100
        enemydmg = 8
    battle = 1
    cls()
    print("You found a(n) " + enemy + "!")  
    time.sleep(1.5)
    print()
    while battle == 1:
        cls()
        print("YOUR TURN")
        cls()
        if enemy == "GEBLIN":
            print("    ____"   )
            print("   |0\/0|  ")
            print("   |^^^^| ")
            print("   /____\  ")
            print("  /|    |\ ")
            print(" | |____| | ")
            print("   d    b ")
            print(" ")

        elif enemy == "BULLTROLL":
            print("    ____    ")
            print("   /0\/0\ ")
            print("   | OO |  ")
            print("    \__/   "   )
            print("    /  \ ")
            print(" ||/    \|| ")
            print("|| |    | || ")
            print("|| |    | || ")
            print("|| |    | ||")
            print("() ||  || () ")
            print("   ||  ||  \ ")
            print("   ||  ||   \ ")
            print("   ||  ||    \ ")
            print("   ||  ||     \ ")
            print("   ||  ||      \ ")
            print("   __  __       {} ")
            print("")
        if enemy == "HAIRIMP":
            print("    _____"   )
            print("   /     \  ")
            print("  / *   * \ ")
            print("/ \  w w  / \   ")
            print("|  \_^_^_/  |" )
            print("|   /   \   |")
            print("   |     |")
            print("   _     _ ")
            print("")
            print(" ")

        elif enemy == "WARRACK":
            print("    __")
            print("   |00\_   ")
            print("   |    |> ")
            print("    \  / ")
            print("     ||   "   )
            print("     ||  ")
            print("     ||  ")
            print("     || ")
            print("    |  | ")
            print("    |__| ")
            print("   ||  ||  ")
            print("   ||  ||   ")
            print("   ||  ||   ")
            print("   ||  ||     ")
            print("   ||  ||      ")
            print("   ||  ||       ")
            print("   ___  ___   ")
            print("")
        elif enemy == "BOMBLOONS":
            print("    _____"   )
            print("   /     \  ")
            print("  /       \ ")
            print("  \       /    ")
            print("   \_____/  " )
            print("      |     ")
            print("  / _i|__ \ ")
            print(" o |     | o  ")
            print("   \_____/   ")
            print(" / ")
            print("o      ")
            print("")
        elif enemy == "ZORBO":
            print("   ______"   )
            print("  / 0  0 \ ")
            print(" /________\ ")
            print("")
        elif enemy == "GHOSTWOOD":
            print("    ")
            print("              _____"   )
            print("             /     \  ")
            print("            /       \ ")
            print("            \       /         _ ")
            print("     ______  \_____/ ________/\ \ " )
            print("           \  |  |  / "   )
            print("            \ |  | / ")
            print("             \|  |/  ")             
            print("              |  | ")
            print("              |  | ")
            print("              |  | ")
            print("              |  | ")
            print("              |  |  ")
            print("              |  |            ")
            print("              |  |      ")
            print("             /    \          ")
            print("            /______\       ")
            print("     ")
            print("")
        elif enemy == "BATTRAX":
            print("         ___  _____  __"   )
            print("     ___/   \/     \/  \___ ")
            print("     \_____ / 0   0 \_____/")
            print("          / \  vvv  / \   ")
            print("          |  \_^^^_/  |" )
            print("          |   /   \   | ")
            print("             |     |   ")
            print("             _     _       ")
            print("")
            print(" ")
        
        elif enemy == "THE TRICKSTER GOD DREVA":
            print("              ____")
            print("             /0000\       ")
            print("             vvvvvv      ")
            print("                             ")
            print("             ^^^^^^ "   )
            print("  ____         ||         ____")
            print("    /  \      /  \      /  \ ")
            print("        \    /|  |\    /")
            print("         \  / |  | \  /")
            print("          \/  \__/  \/ ")
            print("              /  \ ")
            print("             /    \ ")
            print("            /      \ ")
            print("            \      /")
            print("             \    /     ")
            print("             /    \ ")
            print("            /      \ ")
                
        
        if upgrade_counter < 0:
            upgrade_counter = upgrade_counter = 0 
        print("YOUR Health: " + str(health) + " | " + enemy + " Health: " + str(enemy_health))
        print()
        print("Basic ATTACK|Damage:" + str(dmg) + "|Acuracy:100%") 
        print("BASIC MAGIC |Damage:" + str(magic_damage) + "|Acuracy:70%")
        print("Magic Heal|+7HP|Acuracy:100%")
        print("Floor|" + str(upgrade_counter))
        print("GOLD: " + str(goldmax))
        print()
        attack_choice = input("Do you want to ATTACK(1) or MAGIC(2) or RUN(9)? ")
        if attack_choice == "1":
            print()
            print("You ATTACK the " + enemy + "!")
            time.sleep(.8)
            enemy_health = enemy_health - dmg
            if enemy_health <= 0:
                print("You killed the " + enemy + " !" )
                goldmax += gold
                print("You gained " + str(gold) + " GOLD! ")
                time.sleep(1)
                cls()
                print("YOU WON. ")
                upgrade_counter = upgrade_counter + 1
                time.sleep(1.5)
                break
                battle = 0

        
        elif attack_choice == "2":
            print()
            magic_type = input("What MAGIC will you use? FIRE(1) or HEAL(2) ")
            if magic_type == "1":
                print("You FIRE the " + enemy + "!")
                time.sleep(.8)
                chance_hit = random.randint(1,100)
                if chance_hit <= 70:
                    enemy_health  = enemy_health - magic_damage
                    print("You did " + str(magic_damage) + " damage!")
                    if enemy_health <= 0:
                        print("You killed the " + enemy + " !" )
                        goldmax += gold
                        print("You gained " + str(gold) + " GOLD! ")
                        time.sleep(1)
                        cls()
                        print("YOU WON. ")
                        upgrade_counter = upgrade_counter + 1
                        break
                        battle = 0
                        time.sleep(1)
                else:
                    print("You missed your attack!")
            elif magic_type == "2":
                health = health + 7
                while health > max_health:
                    health = health - 1
                print("You Healed! ")
                time.sleep(1.5)
            else:
                print("You missed.")
                time.sleep(1.5)
        elif attack_choice == "9":
            print("You ran away!")
            upgrade_counter = upgrade_counter + 0
            time.sleep(1.5)
            break
            battle = 0
        print()
        print(enemy + "'S " + "TURN")
        print("The " + enemy + " atacks!")
        time.sleep(0.8)
        chance_hit = random.randint(1,100)
        if chance_hit <= 70:
            health = health - enemydmg
            print("The enemy did 3 damage!")
            time.sleep(1.5)
            if health <= 0:
                cls()
                print("YOU DIED!")
                print("GAME OVER")
                play_again = int(input("Would you like to play again? Yes(1) or No(2)"))
                if play_again == 1:
                    health = 10
                    upgrade_counter = 0
                    break
                elif play_again == 2:
                    main.main()
        else:
            time.sleep(.8)
            print("The " + enemy + " missed his attack!")
            time.sleep(1.5)
            cls()
        time.sleep(.8)
    print("The battle has ended. ")
    time.sleep(1)
    print()
    print()
    if upgrade_counter % 5 == 0:
        if upgrade_counter != 0:
            upgrade_choice = input("would you like to upgrade health(1) or damage(2)? ")
            if upgrade_choice == "1":
                max_health = max_health + 4
                print("Your max health is now " + str(max_health) + "!")
                time.sleep(1.5)
            elif upgrade_choice == "2":
                type_of_damage = input("ATTACK(1) or FIRE(2)")
                if type_of_damage == "1":
                    dmg = dmg + 2
                if type_of_damage == "2":
                    magic_damage = magic_damage + 2
        if upgrade_counter == 5:
            enemy_list.append("WARRACK")
            enemy_list.append("BOMBLOONS")
            enemy_list.remove("ZORBO")
        if upgrade_counter == 10:
            enemy_list.append("BULLTROLL")
            enemy_list.append("GHOSTWOOD")
        if upgrade_counter == 15:         #Makes different enemy types more common later on
            enemy_list.append("BATTRAX")
            enemy_list.remove("GEBLIN")
        if upgrade_counter == 20:
            enemy_list.append("THE TRICKSTER GOD DREVA")
