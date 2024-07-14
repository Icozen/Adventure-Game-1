# # # # # Plans For Future
# # # # 1. Using the Inquirerpy module instead of the input() function.

# # # # # New Features
# # # # 1. Added a button to Check the player's Stats, which included hp, dmg, and drops (with their chances), along with bag data.

# # # # # Bug Fixes
# # # # 1. 

# # # # # Other Changes
# # # # 1. 

# # # # # Change In Code
# # # # 1. Put the while loop into a function to save insanity.

# # # # # # # Lines of code: 202 ( - 40 )

import random as r
from time import sleep

class Enemy:
    global enemy
    enemy = []
    def __init__(self, name, hp, req):
        self.name = name
        self.hp = hp
        self.req = req
    def add(self):
        enemy.append(self.name)
        global eencountered
        eencountered = enemy[r.randint(0, (len(enemy) - 1))]

class Item:
    global bag
    bag = []
    def __init__(self, name, num, effect):
        self.name = name
        self.num = num
        self.effect = effect
    def addInBag(self):
        bag.append(self.name)
    def print(self):
        if (len(bag) > 0):
            for index, item in enumerate(bag, 1):
                print(f"{index}. {item}")
            global use
            use = input("What will you use? ")
        else:
            raise IndexError("Empty Bag")

class Chance:
    def __init__(self, name, perc):
        self.name = name
        self.perc = perc

PlayerHP = 150
PlayerDMG = r.randint(20, 30)
PlayerDefense = 0
PlayerEHP = (PlayerHP * (1 + (PlayerDefense / 100)))
EnemyDMG = r.randint(1, 15)
CritDMG = 150                                  # In Percentage
CritHit = int(PlayerDMG * (CritDMG / 100))
Kills = 0
Chance100 = r.randint(1, 100)
SPCounter = 4

aa = Enemy("Assassin", 70, 0)
aa.add()
bb = Enemy("Zombie", 100, 5)
bb.add()
cc = Enemy("Skeleton", 150, 10)
cc.add()
dd = Enemy("Dungeon Warrior", 250, 20)
dd.add()

A = Item("Health Potion", 3, 30)
A.addInBag()
B = Item("Strength Potion", 2, 20)
B.addInBag()
C = Item("Critical Token", 1, 50)
C.addInBag()
# print(bag)

healthpotion = Chance("Health Potion", 20)
crithit = Chance("Critical Hit", 25)
crittoken = Chance("Critical Token", 10)
strengthpotion = Chance("Strength Potion", 5)


# # # # # Functions
# # # 1. Turns
def turn():
    print("-----------------------------")
    print("|\tLoading Game!\t    |")
    print("-----------------------------")
    sleep(3)
    print("---------------------------------------")
    print("\tWelcome To The Dungeon!")
    print("---------------------------------------")
    print("Important Note: All instructions must be given in numbers!")
    print(f"You encountered a {eencountered}!")
    while (True):
        global SPCounter
        global Kills
        global PlayerHP
        global CritDMG
        global CritHit
        SPCounter = SPCounter + 1
        PlayerDMG = r.randint(20, 30)
        CritHit = PlayerDMG * (CritDMG / 100)
        EnemyDMG = r.randint(1, 15)
        Chance100 = r.randint(1, 100)
        a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Use an Item \n3. Run \n"))
        if (a == 1):
                if (SPCounter <= 3):
                    PlayerDMG = PlayerDMG + 20
                    CritHit = PlayerDMG * (CritDMG / 100)
                if (Chance100 <= crithit.perc):
                    PlayerHP = PlayerHP - EnemyDMG
                    aa.hp = aa.hp - int(CritHit)
                    print("A critical hit!")
                    print(f"You dealt {int(CritHit)} DMG to the {eencountered}! It now has {aa.hp} HP left!")
                    print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                    if (PlayerHP <= 0 and aa.hp <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        break
                    elif (PlayerHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        break
                    elif (aa.hp <= 0):
                        c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
                        if (c == 1):
                            Kills = Kills + 1
                            if (Chance100 > healthpotion.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 > crittoken.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}")
                            elif (Chance100 <= crittoken.perc):
                                aa.hp = 70
                                C.num = C.num + 1
                                print(f"The enemy dropped a Critical Token! You now have {A.num} Critical Tokens!")
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 <= healthpotion.perc):
                                aa.hp = 70
                                A.num = A.num + 1
                                print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                                print(f"You encountered a {eencountered}!")
                        else:
                            # print("You left the dungeon, successful in your quest!")
                            print("You got tried of these small-fry and hence, went away!")
                            break
                else:
                    PlayerHP = PlayerHP - EnemyDMG
                    aa.hp = aa.hp - PlayerDMG
                    print(f"You dealt {PlayerDMG} DMG to the {eencountered}! It now has {aa.hp} HP left!")
                    print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                    if (PlayerHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        break
                    if (aa.hp <= 0):
                        c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
                        if (c == 1):
                            Kills = Kills + 1
                            if (Chance100 > healthpotion.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 <= healthpotion.perc):
                                A.num = A.num + 1
                                aa.hp = 70
                                print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                                print(f"You encountered a {eencountered}!")
                        elif (c == 2):
                            print("You left the dungeon, successful in your quest!")
                            break
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        elif (a == 2):
                A.print()
                if (use == "1"):
                    if (A.num > 0):
                        PlayerHP = PlayerHP + A.effect
                        A.num = A.num - 1
                        print(f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!")
                        print(f"You now have {A.num} Health Potions left!")
                    elif (A.num <= 0):
                        print("You don't have any Health Potions left!")
                elif (use == "2"):
                    if (B.num > 0):
                        SPCounter = 0
                        PlayerDMG = PlayerDMG + B.effect
                        B.num = B.num - 1
                        print(f"You used a Strength Potion! It increased your damage by 20!")
                        print(f"You now have {B.num} Strength Potions left!")
                    elif (B.num <= 0):
                        print("You don't have any Strength Potions Tokens left!")
                    pass
                elif (use == "3"):
                    if (C.num > 0):
                        CritDMG = CritDMG + C.effect
                        C.num = C.num - 1
                        print(f"You used a Critical Token! It increased your critical damage by 50%!")
                        print(f"You now have {C.num} Critical Tokens left!")
                    elif (C.num <= 0):
                        print("You don't have any Critical Tokens left!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
        else:
            print("You ran away in fear!")
            break

# # # # # Game Code
print("-----------------------------------")
d = int(input("Do you want to play?\n1. Yes\n2. No\n"))
print("-----------------------------------")
if (d == 1):
    e = int(input("Anything to do first? \n1. Check my Stats \n2. Just Start the Game\n"))
    if (e == 1):
        print("-----------------------------------")
        print("\tStats")
        print("-----------------------------------")
        print(f"Health = {PlayerHP}")
        print(f"Defense = {PlayerDefense}")
        print(f"Effective Max Health = {PlayerEHP}")
        print(f"Damage = {PlayerDMG}")
        print(f"Health Potion Drop Chance = {healthpotion.perc}")
        print(f"Health Potion Effect = {A.effect}")
        print(f"Strength Potion Drop Chance = {strengthpotion.perc}")
        print(f"Strength Potion Effect = {B.effect}")
        print(f"Critical Token Drop Chance = {crittoken.perc}")
        print(f"Critical Token Effect = {C.effect}")
        f = int(input("\nStart now?\n1. Yes\n"))
        if (f == 1):
            turn()
        pass
    else:
        turn()

print(f"You killed {Kills} enemies!")






















































# # # # Variables
# # # Player
# # PlayerHP = 150
# # PlayerDMG = r.randint(20, 30)
# # # Enemy
# # Enemy = ["Zombie", "Skeleton", "Dungeon Warrior", "Assassin"]
# # EEncountered = Enemy[r.randint(0, 3)]          # EnemyEncountered
# # EnemyHP = 70
# # EnemyDMG = r.randint(1, 15)
# # # Other
# # Kills = 0
# # Potions = ["Health", "Strength", "Critical", "Weakness", "Poison"]
# # HPPots = 3
# # HPDC = 20                                      # HealthPotionDropChance
# # HPE = 30                                       # HealthPotionEffect
# # SPots = 2
# # SPDC = 5                                       # StrengthPotionDropChance
# # SPE = 20                                       # StrengthPotionEffect
# # CPots = 1
# # CHC = 30                                       # CriticalHitChance
# # CritDMG = 150                                  # In Percentage
# # CritHit = int(PlayerDMG * (CritDMG / 100))
# # WPots = 1
# # PPots = 1
# # Chance100 = r.randint(1, 100)
# # i = 0
# # j = 0
# # # # Functions
# # # # Game Code
# # print("-----------------------------------")
# # d = int(input("Do you want to play?\n1. Yes\n2. No\n"))
# # print("-----------------------------------")
# # if (d == 1):
# #     print("-----------------------------")
# #     print("|\tLoading Game!\t    |")
# #     print("-----------------------------")
# #     sleep(3)
# #     print("---------------------------------------")
# #     print("\tWelcome To The Dungeon!")
# #     print("---------------------------------------")
# #     print("Important Note: All instructions must be given in numbers!")
# #     print(f"You encountered a {EEncountered}!")
# #     while (i < 1 and j == 0):
# #             CritHit = PlayerDMG * (CritDMG / 100)
# #             PlayerDMG = r.randint(20, 30)
# #             EnemyDMG = r.randint(1, 15)
# #             Chance100 = r.randint(1, 100)
# #             a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Drink a Potion \n3. Run \n"))
# #             if (a == 1):
# #                 if (Chance100 <= CHC):
# #                     PlayerHP = PlayerHP - EnemyDMG
# #                     EnemyHP = EnemyHP - int(CritHit)
# #                     print("A critical hit!")
# #                     print(f"You dealt {int(CritHit)} DMG to the {EEncountered}! It now has {EnemyHP} HP left!")
# #                     print(f"The {EEncountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
# #                     if (PlayerHP <= 0 and EnemyHP <= 0):
# #                         print("\tYou are too weak to move on, so you escape!")
# #                         i = i + 1
# #                         j = j + 1
# #                     elif (PlayerHP <= 0):
# #                         print("\tYou are too weak to move on, so you escape!")
# #                         i = i + 1
# #                         j = j + 1
# #                     elif (EnemyHP <= 0):
# #                         c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
# #                         if (c == 1):
# #                             Kills = Kills + 1
# #                             if (Chance100 > HPDC):
# #                                 EnemyHP = 70
# #                                 EEncountered = Enemy[r.randint(0, 3)]
# #                                 print(f"You encountered a {EEncountered}!")
# #                             elif (Chance100 <= HPDC):
# #                                 HPPots = HPPots + 1
# #                                 EnemyHP = 70
# #                                 EEncountered = Enemy[r.randint(0, 3)]
# #                                 print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
# #                                 print(f"You encountered a {EEncountered}!")
# #                         else:
# #                             print("You left the dungeon, successful in your quest!")
# #                             i = i + 1
# #                             j = j + 1
# #                 else:
# #                     PlayerHP = PlayerHP - EnemyDMG
# #                     EnemyHP = EnemyHP - PlayerDMG
# #                     print(f"You dealt {PlayerDMG} DMG to the {EEncountered}! It now has {EnemyHP} HP left!")
# #                     print(f"The {EEncountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
# #                     if (PlayerHP <= 0):
# #                         print("\tYou are too weak to move on, so you escape!")
# #                         i = i + 1
# #                         j = j + 1
# #                     if (EnemyHP <= 0):
# #                         c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
# #                         if (c == 1):
# #                             Kills = Kills + 1
# #                             if (Chance100 > HPDC):
# #                                 EnemyHP = 70
# #                                 EEncountered = Enemy[r.randint(0, 3)]
# #                                 print(f"You encountered a {EEncountered}!")
# #                             elif (Chance100 <= HPDC):
# #                                 HPPots = HPPots + 1
# #                                 EnemyHP = 70
# #                                 EEncountered = Enemy[r.randint(0, 3)]
# #                                 print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
# #                                 print(f"You encountered a {EEncountered}!")
# #                         elif (c == 2):
# #                             print("You left the dungeon, successful in your quest!")
# #                             i = i + 1
# #                             j = j + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #             elif (a == 2):
# #                 for index, item in enumerate(Potions, 1):
# #                     print(f"{index}. {item}")
# #                 b = input("Which potion to drink? ")
# #                 if (b == "1"):
# #                     if (HPPots > 0):
# #                         PlayerHP = PlayerHP + HPE
# #                         HPPots = HPPots - 1
# #                         print(f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!")
# #                         print(f"You now have {HPPots} Health Potions left!")
# #                     elif (HPPots <= 0):
# #                         print("You don't have any Health Potions left!")
# #                 elif (b == "2"):
# #                     if (SPots > 0):
# #                         PlayerDMG = PlayerDMG + SPE
# #                         SPots = SPots - 1
# #                         print(f"You drank a Stength Potion! It increased your damage by 20 DMG!")
# #                         print(f"You now have {SPots} Strength Potions left!")
# #                 elif (b == "3"):
# #                     pass
# #                 elif (b == "4"):
# #                     pass
# #                 elif (b == "5"):
# #                     pass
# #                 else:
# #                     print("\tNot in the game yet!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# #             else:
# #                 print("You ran away!")
# #                 i = i + 1
# #                 j = j + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # One comment 1. or 2.
# # elif (d == 2):                                                  # 1.
# #     print("Okay! Don't play! Not like I care!")                 # 1.
# # else:                                                           # 1.
# #     raise ValueError ("Your input isn't 1 or 2!")               # 1.

# # # else:                                                           # 2.
# # # print("Okay! Don't play! Not like I care!")                     # 2.

# # print(f"You killed {Kills} enemies!")
