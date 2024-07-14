# # # # # Plans For Future
# # # # 1. 

# # # # # New Features
# # # # 1. "Coloured Drops" setting
# # # # 2. Healing over time
# # # # 3. 

# # # # # Bug Fixes
# # # # 1. 

# # # # # Other Changes
# # # # 1. Decreased effect of HP potions by 5
# # # # 2. Increased enemy damage
# # # # 3. Increased ALL chances by 5%
# # # # 4. 

# # # # # Change In Code
# # # # 1. 

# # # # # # # Lines of code: 353 ( + 27 )

import random as r
from time import sleep
from InquirerPy import prompt
import os
from termcolor import colored
from sounds import *

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
            # for index, item in enumerate(bag, 1):
            #     print(f"{index}. {item}")
            # global use
            # use = input("What will you use? ")
            # def PrintItems():
            #     for index, item in enumerate(bag, 1):
            #         print(f"{index}. {item}")
            ItemUse = [
                {
                    "name": "item",
                    "type": "list",
                    "choices": bag,
                    "message": "Which item do you want to use?"
                }
            ]
            result6 = prompt(ItemUse)
            global use
            use = result6["item"]
            pass
        else:
            raise IndexError("Empty Bag")

class Chance:
    def __init__(self, name, perc):
        self.name = name
        self.perc = perc

PlayerHP = 150
PlayerDMG = r.randint(20, 30)
PlayerDefence = 0
PlayerEHP = (PlayerHP * (1 + (PlayerDefence / 100)))
EnemyDMG = r.randint(10, 20)
CritDMG = 150                                  # In Percentage
CritHit = int(PlayerDMG * (CritDMG / 100))
Kills = 0
Chance100 = r.randint(1, 100)
SPCounter = 4
settings = []

aa = Enemy("Assassin", 70, 0)
aa.add()
bb = Enemy("Zombie", 100, 5)
bb.add()
cc = Enemy("Skeleton", 150, 10)
cc.add()
dd = Enemy("Dungeon Warrior", 250, 20)
dd.add()

A = Item("Health Potion", 3, 25)
A.addInBag()
B = Item("Strength Potion", 2, 20)
B.addInBag()
C = Item("Critical Token", 1, 50)
C.addInBag()
# print(bag)

healthpotion = Chance("Health Potion", 25)
crithit = Chance("Critical Hit", 30)
crittoken = Chance("Critical Token", 15)
strengthpotion = Chance("Strength Potion", 10)

# # # # # Functions
# # # 1. Turns
def turn(*settings):
    print("-----------------------------")
    print("|\tLoading Game!\t    |")
    print("-----------------------------")
    sleep(3)
    print("---------------------------------------")
    print("\tWelcome To The Dungeon!")
    print("---------------------------------------")
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
        whattodo = [
          {
            "name": "turn",
            "type": "list",
            "choices": ["Attack", "Use an Item", "Run"],
            "message": "What to do?",	
          }
        ]
        result1 = prompt(whattodo)
        a = result1["turn"]
        if (a == "Attack"):
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
                        Kills += 1
                        Continue = [
                            {
                                "name": "c0ntinue",
                                "type": "list",
                                "choices": ["Continue", "Escape"],
                                "message": "You defeated the enemy! What to do now?"
                            }
                        ]
                        result2 = prompt(Continue)
                        c = result2["c0ntinue"]
                        if (c == "Continue"):
                            if ("Console Clearing" in settings):
                                os.system("cls")
                                # print("\033c")
                            if (Chance100 > healthpotion.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 > strengthpotion.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}")
                            elif (Chance100 > crittoken.perc):
                                aa.hp = 70
                                print(f"You encountered a {eencountered}")
                            elif (Chance100 <= healthpotion.perc):
                                aa.hp = 70
                                A.num = A.num + 1
                                if ("Coloured Drops" in settings):
                                    print(colored(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!", "red"))
                                else:
                                    print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 <= strengthpotion.perc):
                                aa.hp = 70
                                B.num = B.num + 1
                                if ("Coloured Drops" in settings):
                                    print(colored(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!", "orange"))
                                else:
                                    print(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!")
                                print(f"You encountered a {eencountered}!")
                            elif (Chance100 <= crittoken.perc):
                                aa.hp = 70
                                C.num = C.num + 1
                                if ("Coloured Drops" in settings):
                                    print(colored(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!", "blue"))
                                else:
                                    print(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!")
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
                    Kills += 1
                    Continue = [
                        {
                            "name": "c0ntinue",
                            "type": "list",
                            "choices": ["Continue", "Escape"],
                            "message": "You defeated the enemy! What to do now?"
                        }
                    ]
                    result2 = prompt(Continue)
                    c = result2["c0ntinue"]
                    if (c == "Continue"):
                        if ("Console Clearing" in settings):
                            os.system("cls")
                            # print("\033c")
                        if (Chance100 > healthpotion.perc):
                            aa.hp = 70
                            print(f"You encountered a {eencountered}!")
                        elif (Chance100 > strengthpotion.perc):
                            aa.hp = 70
                            print(f"You encountered a {eencountered}!")
                        elif (Chance100 > crittoken.perc):
                            aa.hp = 70
                            print(f"You encountered a {eencountered}")
                        elif (Chance100 <= healthpotion.perc):
                            aa.hp = 70
                            A.num += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!", "red"))
                            else:
                                print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                            print(f"You encountered a {eencountered}!")
                        elif (Chance100 <= strengthpotion.perc):
                            aa.hp = 70
                            B.num += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!", "orange"))
                            else:
                                print(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!")
                            print(f"You encountered a {eencountered}!")
                        elif (Chance100 <= crittoken.perc):
                            aa.hp = 70
                            C.num += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!", "blue"))
                            else:
                                print(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!")
                            print(f"You encountered a {eencountered}!")
                    else:
                        # print("You left the dungeon, successful in your quest!")
                        print("You got tried of these small-fry and hence, went away!")
                        break

            PlayerHP += 5
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        elif (a == "Use an Item"):
                A.print()
                if (use == "Health Potion"):
                    if (A.num > 0):
                        PlayerHP = PlayerHP + A.effect
                        A.num = A.num - 1
                        print((f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!"))
                        print(f"You now have {A.num} Health Potions left!")
                    elif (A.num <= 0):
                        print("You don't have any Health Potions left!")
                elif (use == "Strength Potion"):
                    if (B.num > 0):
                        SPCounter = 0
                        PlayerDMG = PlayerDMG + B.effect
                        B.num = B.num - 1
                        print(f"You used a Strength Potion! It increased your damage by 20!")
                        print(f"You now have {B.num} Strength Potions left!")
                    elif (B.num <= 0):
                        print("You don't have any Strength Potions Tokens left!")
                    pass
                elif (use == "Critical Token"):
                    if (C.num > 0):
                        CritDMG = CritDMG + C.effect
                        C.num = C.num - 1
                        print(f"You used a Critical Token! It increased your critical damage by 50%!")
                        print(f"You now have {C.num} Critical Tokens left!")
                    elif (C.num <= 0):
                        print("You don't have any Critical Tokens left!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        else:
            print("You ran away in fear!")
            break

# # # # # Game Code
print("-----------------------------------")
play = [
    {
        "name": "PoN",
        "type": "list",
        "choices": ["Yes", "No"],
        "message": "Do you want to play"
    }
]
result3 = prompt(play)
d = result3["PoN"]
print("-----------------------------------")
if (d == "Yes"):
    stats = [
        {
            "name": "stata",
            "type": "list",
            "choices": ["Check my Stats", "Settings", "Just Start the Game"],
            "message": "Anything to do first?"
        }
    ]
    result4 = prompt(stats)
    e = result4["stata"]
    if (e == "Check my Stats"):
        print("-----------------------------------")
        print("\tStats")
        print("-----------------------------------")
        print(f"Health = {PlayerHP}")
        print(f"Defence = {PlayerDefence}")
        print(f"Effective Max Health = {PlayerEHP}")
        print(f"Damage = {PlayerDMG}")
        print(f"Health Potion Drop Chance = {healthpotion.perc}")
        print(f"Health Potion Effect = {A.effect}")
        print(f"Strength Potion Drop Chance = {strengthpotion.perc}")
        print(f"Strength Potion Effect = {B.effect}")
        print(f"Critical Token Drop Chance = {crittoken.perc}")
        print(f"Critical Token Effect = {C.effect}")
        afterstats = [
            {
                "name": "afterstata",
                "type": "list",
                "choices": ["Yes", "No"],
                "message": "Start now?"
            }
        ]
        result5 = prompt(afterstats)
        f = result5["afterstata"]
        if (f == "Yes"):
            turn(*settings)
    elif (e == "Settings"):
        print("-----------------------------------")
        print("\tSettings")
        print("-----------------------------------")
        print("Toggle On?")
        consoleclearing = [
            {
                "name": "console.clear()",
                "type": "confirm",
                "message": "Console Clearing:",
                "default": True
            }
        ]
        result6 = prompt(consoleclearing)
        g = result6["console.clear()"]
        if (g == True):
            settings.append("Console Clearing")
            print("Console Clearing On")
            # system("say Console Clearing On")
            os.system("start consoleclearing.mp3")
        
        coloreddrops = [
            {
                "name": "color.drops()",
                "type": "confirm",
                "message": "Coloured Drops:",
                "default": True
            }
        ]
        result6 = prompt(coloreddrops)
        g = result6["color.drops()"]
        if (g == True):
            settings.append("Coloured Drops")
            print("Coloured Drops On")
            # system("say Coloured Drops On")
            os.system("start coloureddrops.mp3")
            turn(*settings)
        else:
            turn(*settings)
    else:
        turn(*settings)

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
