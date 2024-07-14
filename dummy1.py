# # # # Plans For Future
# # # # 1. (Maybe) Remove the setting voicelines
# # # # 2. Increase the treasures equippable
# # # # 3. 

# # # # # New Features
# # # # 1. A "Go Back to Home Screen" button, which will send you back to the home screen instead of starting the game.
# # # # 2. Treasures:
# #             > They will be of different rarities (Currently not shown in the interface)
# #             > They will be obtained by different methods, e.g getting a PB of 25 kills (Not implemented, so all are already unlocked)
# #             > You can only equip one of them (Subject to change)
# #             > Each have (more or less) different effects
# #             > Some will be active (Have to be equipped, have a cooldown), others will be passive (Always on)
# #             > This update will add 4:
# #                     >> 1. Perfect Treasure Map; an active epic treasure that when used, will give a random stat increase (MaxHPIncrease not implemented)
# #                     >> 2. Gold Clover Coin; a passive epic treasure that increases ALL chances by 1.5 times
# #                     >> 3. 8-Bit Heart; a "passive" rare treasure that will revive you for 50 HP, but will half your damage after revival
# #                     >> 4. Shiny Brooch; an active rare treasure which when activated, will deal 35 DMG to the opponent, but won't kill it
# # # # 3. 

# # # # # Bug Fixes
# # # # 1. Fixed drops and drop colours
# # # # 2.

# # # # # Other Changes
# # # # 1. Removed Healing Over Time
# # # # 2. Reversed HP Potion gain
# # # # 3. Change Strength Potion colour to yellow
# # # # 4. Changed voiceovers for settings to in-window
# # # # 5. Changed drop chances: 
# #             > HP Potion increased from 25 to 30,
# #             > Crit Token lowered from 15 to 12.5,
# #             > Strength Potion increased from 10 to 20,
# #             > Critical hits increased from 30 to 33.3...
# # # # 6. 

# # # # # Change In Code
# # # # 1. Brought the start menu to a function as a whole
# # # # 2. 

# # # # # # # Lines of code: 353 ( + 27 )

import random as r
from time import sleep
from InquirerPy import prompt
import os
from termcolor import colored
import win32com.client 
import json
# from sounds import *

PlayerHP = 150
pdmglow = 20
pdmghigh = 30
PlayerDMG = r.randint(pdmglow, pdmghigh)
PlayerDefense = 0
PlayerEHP = (PlayerHP * (1 + (PlayerDefense / 500)))
EnemyDMG = r.randint(1, 15)
CritDMG = 150                                  # In Percentage
CritHit = int(PlayerDMG * (CritDMG / 100))
Kills = 0
SPCounter = 4
settings = []
treasureEquipped = []
preferredSettings = 0
HPotionDrops = 0
SPotionDrops = 0
CTokenDrops = 0

AChance100 = r.randint(1, 100)
BChance100 = r.randint(1, 100)
CChance100 = r.randint(1, 100)
speaker = win32com.client.Dispatch("SAPI.SpVoice") 

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
    def __init__(self, name, num, hpincrease, hpcapincrease, dmgincrease, dmgmultiplier, critchanceincrease, critdmgincrease, defenseincrease):
        self.name = name
        self.num = num
        self.hpincrease = hpincrease
        self.hpcapincrease = hpcapincrease
        self.dmgincrease = dmgincrease
        self.dmgmultiplier = dmgmultiplier
        self.critchanceincrease = critchanceincrease
        self.critdmgincrease = critdmgincrease
        self.defenseincrease = defenseincrease
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
        else:
            raise IndexError("Empty Bag")

class Chance:
    def __init__(self, name, perc):
        self.name = name
        self.perc = perc

class Treasure(Item):
    def __init__(self, name: str, rarity: str, activity: str, hpincrease: int, hpcapincrease: float, dmgincrease: int, dmgmultiplier: float, critchanceincrease: int, critdmgincrease: int, defenseincrease: int, damage: int, uniqueability: bool, cooldown: int):
        self.name = name
        self.rarity = rarity
        self.activity = activity

        self.hpincrease = hpincrease
        self.hpcapincrease = hpcapincrease
        self.dmgincrease = dmgincrease
        self.dmgmultiplier = dmgmultiplier
        self.critchanceincrease = critchanceincrease
        self.critdmgincrease = critdmgincrease
        self.defenseincrease = defenseincrease
        self.damage = damage
        if activity != "Active":
            self.cooldown = None
        else:
            self.cooldown = cooldown
        self.uniqueability = uniqueability
    # # # # # Treasure Functions
    # # # 1. Perfect Treasure Map
    def perfect_treasure_map(self):
        global PlayerHP, PlayerDMG, CritDMG, PlayerDefense, pdmghigh, pdmglow
        PTMStatBuff = r.randint(1, 8)
        if PTMStatBuff == 1:
            PlayerHP += PerfectTreasureMap.hpincrease
            print(f"You gained {PerfectTreasureMap.hpincrease} health. You now have {PlayerHP} health remaining.")
        elif PTMStatBuff == 2:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif PTMStatBuff == 3:
            pdmglow += PerfectTreasureMap.dmgincrease
            pdmghigh += PerfectTreasureMap.dmgincrease
            print(f"Your damage increased by {PerfectTreasureMap.dmgincrease}. Your max damage is now {pdmghigh}.")
        elif PTMStatBuff == 4:
            pdmglow = pdmglow * PerfectTreasureMap.dmgmultiplier
            pdmghigh = pdmghigh * PerfectTreasureMap.dmgmultiplier
            print(f"Your damage increased substantially by {PerfectTreasureMap.dmgmultiplier}. Your max damage is now {pdmghigh}.")
        elif PTMStatBuff == 5:
            crithit.perc = crithit.perc * PerfectTreasureMap.critchanceincrease
            print(f"You now are more accurate, dealing more critical hits.")
        elif PTMStatBuff == 6:
            CritDMG = CritDMG * PerfectTreasureMap.critdmgincrease
            print(f"You now hit harder when the attack is a critical hit.")
        elif PTMStatBuff == 7:
            PlayerDefense += PerfectTreasureMap.defenseincrease
            print(f"You're more beefier now.")
        else:
            print("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        return PTMStatBuff
    # # # 2. Gold Clover Coin
    def gold_clover_coin(self):
        healthpotion.perc = healthpotion.perc * 1.5
        crittoken.perc = crittoken.perc * 1.5
        strengthpotion.perc = strengthpotion.perc * 1.5
        crithit.perc = crithit.perc * 1.5
    # # # 3. 8-Bit Heart
    def eight_bit_heart(self):
        if PlayerHP <= 0:
            PlayerHP = 50
            PlayerDMG = PlayerDMG / 2
            print(f"You have been revived, in exchange of half of your damage. You now have {PlayerHP} health remaining.")
    # # # 4. Shiny Brooch
    def shiny_brooch(self):
        if self.uniqueability:
            Zombie.hp -= 30

Zombie = Enemy("Zombie", 70, 0)
Zombie.add()
Skeleton = Enemy("Skeleton", 100, 5)
Skeleton.add()
Assassin = Enemy("Assassin", 150, 10)
Assassin.add()
DungeonWarrior = Enemy("Dungeon Warrior", 250, 20)
DungeonWarrior.add()

A = Item("Health Potion", 3, 30, 0, 0, 0, 0, 0, 0,)
A.addInBag()
B = Item("Strength Potion", 2, 0, 0, 20, 0, 0, 0, 0)
B.addInBag()
C = Item("Critical Token", 1, 0, 0, 0, 0, 0, 50, 0)
C.addInBag()
# print(bag)

crithit = Chance("Critical Hit", 100/3)
healthpotion = Chance("Health Potion", 30)
crittoken = Chance("Critical Token", 12.5)
strengthpotion = Chance("Strength Potion", 20)
# healthpotion = Chance("Health Potion", 37.5)
# crittoken = Chance("Critical Token", 22.5)
# strengthpotion = Chance("Strength Potion", 15)

PerfectTreasureMap = Treasure("Perfect Treasure Map", "Epic", "Active", 15, 1.2, 10, 1.2, 4, 50, 100, 30, False, 7)
GoldCloverCoin = Treasure("Gold Clover Coin", "Epic", "Passive", 0, 0, 0, 0, 0, 0, 0, 0, True, 0)
EightBitHeart = Treasure("8-Bit Heart", "Rare", "Passive", 0, 0, 0, 0, 0, 0, 0, 0, True, 0)
ShinyBrooch = Treasure("Shiny Brooch", "Rare", "Active", 0, 0, 0, 0, 0, 0, 0, 35, False, 3)

goback = [
    {
        "name": "BackToHomeScreen",
        "type": "list",
        "choices": ["Yes", "No"],
        "message": "Go back to Home Screen"
    }
]

stats = [
    {
        "name": "stata",
        "type": "list",
        "choices": ["Treasures (Mandatory)", "Check my Stats", "Settings", "Just Start the Game"],
        "message": "Anything to do first?"
    }
]

Continue = [
    {
        "name": "c0ntinue",
        "type": "list",
        "choices": ["Continue", "Escape"],
        "message": "You defeated the enemy! What to do now?"
    }
]

Equip = [
    {
        "name": "Treasure2Equip",
        "type": "list",
        "choices": ["     - Perfect Treasure Map", "     - Gold Clover Coin", "     - 8-Bit Heart", "     - Shiny Brooch"],
        "message": "Equip treasure(s):"
    }
]

# # # # # Functions
# # # 1. Turns
def turn(settings, treasureEquipped):
    print("-----------------------------")
    print("|\tLoading Game!\t    |")
    print("-----------------------------")
    sleep(3)
    print("---------------------------------------")
    print("\tWelcome To The Dungeon!")
    print("---------------------------------------")
    print(f"You encountered a {eencountered}!")
    if (treasureEquipped[0] == "Gold Clover Coin"):
        GoldCloverCoin.gold_clover_coin()
    shinebrooch = False
    while (True):
        global SPCounter, HPotionDrops, SPotionDrops, CTokenDrops, Kills, PlayerHP, CritDMG, CritHit
        SPCounter = SPCounter + 1
        PlayerDMG = r.randint(pdmglow, pdmghigh)
        CritHit = PlayerDMG * (CritDMG / 100)
        EnemyDMG = r.randint(1, 15)
        AChance100 = r.randint(1, 100)
        BChance100 = r.randint(1, 100)
        CChance100 = r.randint(1, 100)
        if (treasureEquipped[0] == "Perfect Treasure Map" or treasureEquipped[0] == "Shiny Brooch"): 
            whattodo = [
                {
                    "name": "turn",
                    "type": "list",
                    "choices": ["Attack", f"Use {treasureEquipped[0]}", "Use an Item", "Run"],
                    "message": "What to do?",	
                }
            ]
        else:
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
        if (a == f"Use {treasureEquipped[0]}"):
            if (treasureEquipped[0] == "Perfect Treasure Map"):
                PerfectTreasureMap.perfect_treasure_map()
            elif (treasureEquipped[0] == "Shiny Brooch"):
                shinebrooch = True
                Zombie.hp -= ShinyBrooch.damage
                print(f"The treasure dealt {ShinyBrooch.damage} DMG to the {eencountered}! It now has {Zombie.hp} HP left!")
                # print(f"The treasure dealt {ShinyBrooch.damage} DMG to the {eencountered}! It now has {Zombie.hp} HP left!")
        elif (a == "Attack"):
            if (SPCounter <= 3):
                    PlayerDMG = PlayerDMG + 20
                    CritHit = PlayerDMG * (CritDMG / 100)
            if shinebrooch:
                shinebrooch = False
            if (AChance100 <= crithit.perc):
                    PlayerHP = PlayerHP - EnemyDMG
                    Zombie.hp = Zombie.hp - int(CritHit)
                    print("A critical hit!")
                    print(f"You dealt {int(CritHit)} DMG to the {eencountered}! It now has {Zombie.hp} HP left!")
                    print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                    if (PlayerHP <= 0 and Zombie.hp <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        break
                    elif (PlayerHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        break
                    elif (Zombie.hp <= 0):
                        Kills += 1
                        result2 = prompt(Continue)
                        c = result2["c0ntinue"]
                        if (c == "Continue"):
                            if ("Console Clearing" in settings):
                                os.system("cls")
                                # print("\033c")
                            if (AChance100 > healthpotion.perc):
                                Zombie.hp = 70
                                print(f"You encountered a {eencountered}!")
                            if (AChance100 <= healthpotion.perc):
                                Zombie.hp = 70
                                A.num = A.num + 1
                                HPotionDrops += 1
                                if ("Coloured Drops" in settings):
                                    print(colored(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!", "red"))
                                else:
                                    print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                                print(f"You encountered a {eencountered}!")
                            if (BChance100 <= strengthpotion.perc):
                                Zombie.hp = 70
                                B.num = B.num + 1
                                SPotionDrops += 1
                                if ("Coloured Drops" in settings):
                                    print(colored(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!", "yellow"))
                                else:
                                    print(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!")
                                print(f"You encountered a {eencountered}!")
                            if (CChance100 <= crittoken.perc):
                                Zombie.hp = 70
                                C.num = C.num + 1
                                CTokenDrops += 1
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
                Zombie.hp = Zombie.hp - PlayerDMG
                print(f"You dealt {PlayerDMG} DMG to the {eencountered}! It now has {Zombie.hp} HP left!")
                print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                if (treasureEquipped[0] == "8-Bit Heart"):
                    EightBitHeart.eight_bit_heart()
                elif (PlayerHP <= 0):
                    print("\tYou are too weak to move on, so you escape!")
                    break
                if (Zombie.hp <= 0):
                    Kills += 1
                    result2 = prompt(Continue)
                    c = result2["c0ntinue"]
                    if (c == "Continue"):
                        if ("Console Clearing" in settings):
                            os.system("cls")
                            # print("\033c")
                        if (AChance100 > healthpotion.perc):
                            Zombie.hp = 70
                            print(f"You encountered a {eencountered}!")
                        if (AChance100 <= healthpotion.perc):
                            Zombie.hp = 70
                            A.num += 1
                            HPotionDrops += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!", "red"))
                            else:
                                print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
                            print(f"You encountered a {eencountered}!")
                        if (BChance100 <= strengthpotion.perc):
                            Zombie.hp = 70
                            B.num += 1
                            SPotionDrops += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!", "yellow"))
                            else:
                                print(f"The enemy dropped a Strength Potion! You now have {B.num} Strength Potions!")
                            print(f"You encountered a {eencountered}!")
                        if (CChance100 <= crittoken.perc):
                            Zombie.hp = 70
                            C.num += 1
                            CTokenDrops += 1
                            if ("Coloured Drops" in settings):
                                print(colored(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!", "blue"))
                            else:
                                print(f"The enemy dropped a Critical Token! You now have {C.num} Critical Tokens!")
                            print(f"You encountered a {eencountered}!")
                    else:
                        # print("You left the dungeon, successful in your quest!")
                        print("You got tried of these small-fry and hence, went away!")
                        break
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        elif (a == "Use an Item"):
                A.print()
                if (use == "Health Potion"):
                    if (A.num > 0):
                        PlayerHP = PlayerHP + A.hpincrease
                        A.num = A.num - 1
                        print((f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!"))
                        print(f"You now have {A.num} Health Potions left!")
                    elif (A.num <= 0):
                        print("You don't have any Health Potions left!")
                elif (use == "Strength Potion"):
                    if (B.num > 0):
                        SPCounter = 0
                        PlayerDMG = PlayerDMG + B.dmgincrease
                        B.num = B.num - 1
                        print(f"You used a Strength Potion! It increased your damage by 20!")
                        print(f"You now have {B.num} Strength Potions left!")
                    elif (B.num <= 0):
                        print("You don't have any Strength Potions Tokens left!")
                    pass
                elif (use == "Critical Token"):
                    if (C.num > 0):
                        CritDMG = CritDMG + C.critdmgincrease
                        C.num = C.num - 1
                        print(f"You used a Critical Token! It increased your critical damage by 50%!")
                        print(f"You now have {C.num} Critical Tokens left!")
                    elif (C.num <= 0):
                        print("You don't have any Critical Tokens left!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
        else:
            print("You ran away in fear!")
            break

# # # 2. Start Menu
def start_menu():
    global result4, e
    result4 = prompt(stats)
    e = result4["stata"]
    if (e == "Check my Stats"):
        print("-----------------------------------")
        print("\tStats")
        print("-----------------------------------")
        print(f"Health = {PlayerHP}")
        print(f"Defence = {PlayerDefense}")
        print(f"Effective Max Health = {PlayerEHP}")
        print(f"Damage = {PlayerDMG}")
        print(f"Health Potion Drop Chance = {healthpotion.perc}")
        print(f"Health Potion Effect = {A.hpincrease}")
        print(f"Strength Potion Drop Chance = {strengthpotion.perc}")
        print(f"Strength Potion Effect = {B.dmgincrease}")
        print(f"Critical Token Drop Chance = {crittoken.perc}")
        print(f"Critical Token Effect = {C.critdmgincrease}")
        result7 = prompt(goback)
        f = result7["BackToHomeScreen"]
        if f == "Yes":
            start_menu()
        else:
            turn(settings, treasureEquipped)
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
        if g:
            settings.append("Console Clearing")
            # print("Console Clearing On")
            # system("say Console Clearing On")
            speaker.Speak("Console Clearing On")
            # os.system("start consoleclearing.mp3")
        
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
        if g:
            settings.append("Coloured Drops")
            # print("Coloured Drops On")
            # system("say Coloured Drops On")
            speaker.Speak("Coloured Drops On")
            # os.system("start coloureddrops.mp3")
        
        prefer = [
            {
                "name": "preferSettings",
                "type": "list",
                "choices": ["Yes", "No"],
                "message": "Do you want your settings to be the permanent settings? (Unless changed later)",
            }
        ]
        result9 = prompt(prefer)
        i = result9["preferSettings"]
        if i == "Yes":
            global preferredSettings
            preferredSettings = settings
        else:
            global noChangeOfPreference
            noChangeOfPreference = True
        result7 = prompt(goback)
        f = result7["BackToHomeScreen"]
        if f == "Yes":
            start_menu()
        else:
            turn(settings, treasureEquipped)
    elif (e == "Treasures (Mandatory)"):
        SlotsEquippable = 1
        SlotsEquipped = 0
        print(f"Slots Equippable = {SlotsEquippable}")
        print(f"Slots Equipped = {SlotsEquipped}")
        # print("Treasures: \n     - Perfect Treasure Map\n     - Gold Clover Coin\n     - 8-Bit Heart\n     - Shiny Brooch")
        result8 = prompt(Equip)
        h = result8["Treasure2Equip"]
        if (h == "     - Perfect Treasure Map"):
            SlotsEquippable -= 1
            SlotsEquipped += 1
            treasureEquipped.append("Perfect Treasure Map")
        elif (h == "     - Gold Clover Coin"):
            SlotsEquippable -= 1
            SlotsEquipped += 1
            treasureEquipped.append("Gold Clover Coin")
        elif (h == "     - 8-Bit Heart"):
            SlotsEquippable -= 1
            SlotsEquipped += 1
            treasureEquipped.append("8-Bit Heart")
        elif (h == "     - Shiny Brooch"):
            SlotsEquippable -= 1
            SlotsEquipped += 1
            treasureEquipped.append("Shiny Brooch")
        print(f"Treasure Equipped: {treasureEquipped[0]}")
        result7 = prompt(goback)
        f = result7["BackToHomeScreen"]
        if f == "Yes":
            start_menu()
        else:
            turn(settings, treasureEquipped)
    else:
        turn(settings, treasureEquipped)


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
    start_menu()

print(f"You killed {Kills} enemies!")

if (noChangeOfPreference):
    
    pass

userPreferencesAndPerformances = {
    # "soundEnabled": True,
    "settings": ["Coloured Drops"],
    "unlockedTreasures": ["Shiny Brooch"],
    "unlockedEnemies": ["Zombie"],
    "highestKillCount": 0,
    "healthPotionDrops": 0,
    "strengthPotionDrops": 0,
    "criticalTokenDrops": 0,
}
# # Assuming these variables are defined somewhere in your code
# Kills = 10  # Example value
# HPotionDrops = 5  # Example value
# SPotionDrops = 3  # Example value
# CTokenDrops = 2  # Example value

def savePrefs(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file)

def loadPrefs(filename, data):
    try:
        with open(filename, "r") as file:
            prefs = json.load(file)
            
            # Check if the current game's stats are better than the saved ones
            if data["highestKillCount"] > prefs.get("highestKillCount", 0):
                prefs["highestKillCount"] = data["highestKillCount"]
            if data["healthPotionDrops"] > prefs.get("healthPotionDrops", 0):
                prefs["healthPotionDrops"] = data["healthPotionDrops"]
            if data["strengthPotionDrops"] > prefs.get("strengthPotionDrops", 0):
                prefs["strengthPotionDrops"] = data["strengthPotionDrops"]
            if data["criticalTokenDrops"] > prefs.get("criticalTokenDrops", 0):
                prefs["criticalTokenDrops"] = data["criticalTokenDrops"]
                
            return prefs
    except FileNotFoundError:
        return {}

prefsFilename = "userPrefsNPerfs.json"

# Example usage
data = {
    "settings": preferredSettings,  # Replace {} with actual settings
    "unlockedTreasures": ["Shiny Brooch"],
    "unlockedEnemies": ["Zombie"],
    "highestKillCount": Kills,
    "healthPotionDrops": HPotionDrops,
    "strengthPotionDrops": SPotionDrops,
    "criticalTokenDrops": CTokenDrops,
}

savePrefs(prefsFilename, data)
loaded_prefs = loadPrefs(prefsFilename, data)
print("Best scores and Player preferences:", loaded_prefs)




















############################################################################################################################################################################################################################################################################################################################################################

############################################################################################################################################################################################################################################################################################################################################################
















































































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
