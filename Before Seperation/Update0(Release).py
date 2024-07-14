# # # # # New Features
# # # # 1. 4 different enemies
# # # # 2. Health Potions; start with 3, heals 30 HP, and has a 1/5 chance (20%) to drop one

# # # # # # # Lines of Code: 71

import random as r
# # Variables
# Player
PlayerHP = 150
PlayerDMG = r.randint(20, 30)
# Enemy
Enemy = ["Zombie", "Skeleton", "Dungeon Warrior", "Assassin"]
EEncountered = Enemy[r.randint(0, 3)]          # EnemyEncountered
EnemyHP = 40
EnemyDMG = r.randint(1, 15)
# Other
Potions = ["Health", "Strength", "Critical", "Weakness", "Poison"]
HPPots = 3
HPDC = 20                                      # HealthPotionDropChance
HPE = 30                                       # HealthPotionEffect
SPots = 2
CPots = 1
WPots = 1
PPots = 1
Chance100 = r.randint(1, 100)
i = 0
j = 0
# # Functions
# # Game Code
print("---------------------------------------")
print("\tWelcome To The Dungeon!")
print("---------------------------------------")
print(f"You encountered a {EEncountered}!")
while (i < 1 and j == 0):
  PlayerDMG = r.randint(20, 30)
  EnemyDMG = r.randint(1, 15)
  Chance100 = r.randint(1, 100)
  a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Drink a Potion \n3. Run \n"))
  if (a == 1):
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
          EnemyHP = 40
          EEncountered = Enemy[r.randint(0, 3)]
          print(f"You encountered a {EEncountered}!")
        elif (Chance100 <= HPDC):
          HPPots = HPPots + 1
          EnemyHP = 40
          EEncountered = Enemy[r.randint(0, 3)]
          print(f"The enemy dropped a Health Potion! You now have {HPPots} Health Potions!")
          print(f"You encountered a {EEncountered}!")
      elif (c == 2):
        print("You left the dungeon, successful in your quest!")
        i = i + 1
        j = j + 1
# # # # # # # # # # # # # # # # # # # # # #
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
    else:
      print("Not in the game yet!")
# # # # # # # # # # # # # # # # # # # # # #
  else:
    print("You ran away!")
    i = i + 1
    j = j + 1