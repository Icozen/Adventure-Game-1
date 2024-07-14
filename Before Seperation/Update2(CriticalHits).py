# # # # # New Features
# # # # 1. Critical Hits; has a 3/10 chance (30%), deals 1.5X DMG (150%)
# # # # 2. Loading Screen # 2
# # # # # Change In Code 
# # # # 1. Added an if-else statement in the Attack (a == 1) section

# # # # # # # Lines of code: 135 ( + 51 )

import random as r
from time import sleep
# # Variables
# Player
PlayerHP = 150
PlayerDMG = r.randint(20, 30)
# Enemy
Enemy = ["Zombie", "Skeleton", "Dungeon Warrior", "Assassin"]
EEncountered = Enemy[r.randint(0, 3)]          # EnemyEncountered
EnemyHP = 70
EnemyDMG = r.randint(1, 15)
# Other
Potions = ["Health", "Strength", "Critical", "Weakness", "Poison"]
HPPots = 3
HPDC = 20                                      # HealthPotionDropChance
HPE = 30                                       # HealthPotionEffect
SPots = 2
SPDC = 5                                       # StrengthPotionDropChance
SPE = 20                                       # StrengthPotionEffect
CPots = 1
CHC = 30                                       # CriticalHitChance
CritDMG = 150                                  # In Percentage
CritHit = int(PlayerDMG * (CritDMG / 100))
WPots = 1
PPots = 1
Chance100 = r.randint(1, 100)
i = 0
j = 0
# # Functions
# # Game Code
print("-----------------------------------")
d = int(input("Do you want to play?\n1. Yes\n2. No\n"))
print("-----------------------------------")
if (d == 1):
    print("-----------------------------")
    print("|\tLoading Game!\t    |")
    print("-----------------------------")
    sleep(3)
    print("---------------------------------------")
    print("\tWelcome To The Dungeon!")
    print("---------------------------------------")
    print("Important Note: All instructions must be given in numbers!")
    print(f"You encountered a {EEncountered}!")
    while (i < 1 and j == 0):
            PlayerDMG = r.randint(20, 30)
            CritHit = PlayerDMG * (CritDMG / 100)
            EnemyDMG = r.randint(1, 15)
            Chance100 = r.randint(1, 100)
            a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Drink a Potion \n3. Run \n"))
            if (a == 1):
                if (Chance100 <= CHC):
                    PlayerHP = PlayerHP - EnemyDMG
                    EnemyHP = EnemyHP - int(CritHit)
                    print("A critical hit!")
                    print(f"You dealt {int(CritHit)} DMG to the {EEncountered}! It now has {EnemyHP} HP left!")
                    print(f"The {EEncountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                    if (PlayerHP <= 0 and EnemyHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        i = i + 1
                        j = j + 1
                    elif (PlayerHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        i = i + 1
                        j = j + 1
                    elif (EnemyHP <= 0):
                        c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
                        if (c == 1):
                            if (Chance100 > HPDC):
                                EnemyHP = 70
                                EEncountered = Enemy[r.randint(0, 3)]
                                print(f"You encountered a {EEncountered}!")
                            elif (Chance100 <= HPDC):
                                HPPots = HPPots + 1
                                EnemyHP = 70
                                EEncountered = Enemy[r.randint(0, 3)]
                                print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
                                print(f"You encountered a {EEncountered}!")
                        else:
                            print("You left the dungeon, successful in your quest!")
                            i = i + 1
                            j = j + 1
                else:
                    PlayerHP = PlayerHP - EnemyDMG
                    EnemyHP = EnemyHP - PlayerDMG
                    print(f"You dealt {PlayerDMG} DMG to the {EEncountered}! It now has {EnemyHP} HP left!")
                    print(f"The {EEncountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
                    if (PlayerHP <= 0):
                        print("\tYou are too weak to move on, so you escape!")
                        i = i + 1
                        j = j + 1
                    if (EnemyHP <= 0):
                        c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
                        if (c == 1):
                            if (Chance100 > HPDC):
                                EnemyHP = 70
                                EEncountered = Enemy[r.randint(0, 3)]
                                print(f"You encountered a {EEncountered}!")
                            elif (Chance100 <= HPDC):
                                HPPots = HPPots + 1
                                EnemyHP = 70
                                EEncountered = Enemy[r.randint(0, 3)]
                                print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
                                print(f"You encountered a {EEncountered}!")
                        elif (c == 2):
                            print("You left the dungeon, successful in your quest!")
                            i = i + 1
                            j = j + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            elif (a == 2):
                for index, item in enumerate(Potions, 1):
                    print(f"{index}. {item}")
                b = input("Which potion to drink? ")
                if (b == "1"):
                    if (HPPots > 0):
                        PlayerHP = PlayerHP + HPE
                        HPPots = HPPots - 1
                        print(f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!")
                        print(f"You now have {HPPots} Health Potions left!")
                    elif (HPPots <= 0):
                        print("You don't have any Health Potions left!")
                elif (b == "2"):
                    if (SPots > 0):
                        PlayerDMG = PlayerDMG + SPE
                        SPots = SPots - 1
                        print(f"You drank a Stength Potion! It increased your damage by 20 DMG!")
                        print(f"You now have {SPots} Strength Potions left!")
                elif (b == "3"):
                    pass
                elif (b == "4"):
                    pass
                elif (b == "5"):
                    pass
                else:
                    print("\tNot in the game yet!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            else:
                print("You ran away!")
                i = i + 1
                j = j + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # One comment 1. or 2.
elif (d == 2):                                                  # 1.
    print("Okay! Don't play! Not like I care!")                 # 1.
else:                                                           # 1.
    raise ValueError ("Your input isn't 1 or 2!")               # 1.

# else:                                                           # 2.
# print("Okay! Don't play! Not like I care!")                     # 2.


# # # # # # # # # # # Shit Section

# 1. Put this in front of The first while

        # while (SPots < 2 and i < 1 and j == 0):
#             PlayerDMG = PlayerDMG + SPE
#             EnemyDMG = r.randint(1, 15)
#             Chance100 = r.randint(1, 100)
#             a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Drink a Potion \n3. Run \n"))
#             if (a == 1):
#                 PlayerHP = PlayerHP - EnemyDMG
#                 EnemyHP = EnemyHP - PlayerDMG
#                 print(f"You dealt {PlayerDMG} DMG to the {EEncountered}! It now has {EnemyHP} HP left!")
#                 print(f"The {EEncountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
#                 if (PlayerHP <= 0):
#                     print("\tYou are too weak to move on, so you escape!")
#                     i = i + 1
#                     j = j + 1
#                 if (EnemyHP <= 0):
#                     c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
#                     if (c == 1):
#                         if (Chance100 > HPDC):
#                             EnemyHP = 70
#                             EEncountered = Enemy[r.randint(0, 3)]
#                             print(f"You encountered a {EEncountered}!")
#                         elif (Chance100 <= HPDC):
#                             HPPots = HPPots + 1
#                             EnemyHP = 70
#                             EEncountered = Enemy[r.randint(0, 3)]
#                             print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
#                             print(f"You encountered a {EEncountered}!")
#                     elif (c == 2):
#                         print("You left the dungeon, successful in your quest!")
#                         i = i + 1
#                         j = j + 1
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#             elif (a == 2):
#                 for index, item in enumerate(Potions, 1):
#                     print(f"{index}. {item}")
#                 b = input("Which potion to drink? ")
#                 if (b == "1"):
#                     if (HPPots > 0):
#                         PlayerHP = PlayerHP + HPE
#                         HPPots = HPPots - 1
#                         print(f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!")
#                         print(f"You now have {HPPots} Health Potions left!")
#                     elif (HPPots <= 0):
#                         print("You don't have any Health Potions left!")
#                 elif (b == "2"):
#                     if (SPots > 0):
#                         PlayerDMG = PlayerDMG + SPE
#                         SPots = SPots - 1
#                         print(f"You drank a Stength Potion! It increased your damage by 20 DMG!")
#                         print(f"You now have {SPots} Strength Potions left!")
#                 elif (b == "3"):
#                     pass
#                 elif (b == "4"):
#                     pass
#                 elif (b == "5"):
#                     pass
#                 else:
#                     print("\tNot in the game yet!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#             else:
#                 print("You ran away!")
#                 i = i + 1
#                 j = j + 1
        # else: