# # # # # New Features
# # # # 1. Lowered Crit. Chance to 1/10(10%)

# # # # # Bug Fixes
# # # # 1. Fixed Bug A (Kills by critical hits weren't being counted)

# # # # # Other Changes
# # # # 1. Changed the code type to Object Oriented Programming

# # # # # Change In Code
# # # # 1. Changed entirely to OOP style programming

# # # # # # # Lines of code: 148 ( + 10 )

import pygame
from random import randint, random
from time import sleep
import sys
import sqlite3 as lite

pygame.init()
pygame.display.set_caption("Adventure Game")
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
# pygame.display.set_icon("assets/icon.png")
FPS = 60
font = pygame.font.SysFont('Times New Normal Regular.ttf', 40)
background = pygame.Surface((width, height))
PlayerX = 200
PlayerY = 80
EnemyX = 600
EnemyY = 80
isRunPressed = False
isAttackPressed = False
pygame.draw.rect(background,(0, 0, 255),(PlayerX, PlayerY, 40, 40))
pygame.draw.rect(background,(255, 0, 0), (EnemyX, EnemyY, 40, 40))
textPosAndTime = []
runPopUpSeconds = 3
currentTime = pygame.time.get_ticks()

start = attack = useItem = run = ""

objects = []

class Enemy:
    def __init__(self, name, hp, req):
        self.name = name
        self.hp = hp
        self.req = req
    def add(self):
        global enemy
        enemy = []
        enemy.append(self.name)
        global eencountered
        eencountered = enemy[randint(0, (len(enemy) - 1))]

class Item:
    def __init__(self, name, num, effect):
        self.name = name
        self.num = num
        self.effect = effect
    def addInBag(self):
        global bag
        bag = []
        bag.append(self.name)
    def print(self):
        if (len(bag) > 0):
            for item, index in enumerate(bag, 1):
                print(f"{index}. {item}")
                global use
            use = input("What will you use? ")
        else:
            raise IndexError("Empty Bag")

class Chance:
    def __init__(self, name, perc):
        self.name = name
        self.perc = perc

class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.fillColors = {
            'normal': '#3f48cc',
            'hover': '#008bc8',
            'pressed': '#00a8f3',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        objects.append(self)
    
    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

PlayerHPValue = 150
PlayerDMGValue = randint(20, 30)
EnemyHPValue = 70
EnemyDMGValue = randint(0, 15)
CritDMG = 150                                  # In Percentage
CritHit = int(PlayerDMGValue * (CritDMG / 100))
Kills = 0
Chance100 = randint(1, 100)

aa = Enemy("Zombie", 70, 0)
aa.add()
bb = Enemy("Skeleton", 100, 5)
bb.add()
cc = Enemy("Assassin", 150, 10)
cc.add()
dd = Enemy("Dungeon Warrior", 250, 20)
dd.add()

A = Item("Health Potion", 3, 30)
A.addInBag()

healthpotion = Chance("Health Potion", 20)
crithit = Chance("Critical Hit", 10)

print("-----------------------------------")


def myFunction():
    print('Button Pressed')

def AttackPressed():
    global isAttackPressed
    isAttackPressed = True

def BagPressed():
    pass

def RunPressed():
    global isRunPressed
    global Run
    isRunPressed = True
    Run = font.render("You ran away!", True, (255, 255, 255))
    # textPosAndTime.append(currentTime + runPopUpSeconds * 1000)

B1 = Button(50, 500, 200, 50, 'Attack', AttackPressed)
B2 = Button(300, 500, 200, 50, 'Bag', BagPressed)
B3 = Button(550, 500, 200, 50, 'Run', RunPressed)

# Button(30, 140, 400, 100, 'Button Two (multiPress)', myFunction, True)

PlayerHPText = font.render(f"Your HP: {PlayerHPValue}", True, (255, 255, 255))
EnemyHPText = font.render(f"Enemy's HP: {EnemyHPValue}", True, (255, 255, 255))

def turn():
    global isAttackPressed
    global PlayerHPValue
    if isAttackPressed == True:
        global EnemyHPValue
        PlayerHPValue -= EnemyDMGValue
        EnemyHPValue -= PlayerDMGValue
        isAttackPressed = False
        print("dfxgchvjyg")
    
    # if isBagPressed == True:
    #     PlayerHPValue += 30
    
    if isRunPressed == True:
        screen.blit(Run, (300, 200))
        print("dfxgchvjyg")
        pygame.time.delay(3000)
        isGameRunning = False

def main(screen):
    clock = pygame.time.Clock()

    

    isGameRunning = True
    close = False

    while isGameRunning:
        screen.fill((0, 100, 255))
        # screen.blit("assets/Characters/Player.jpg", (50, 50))
        screen.blit(background, (0, 0))

        turn()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isGameRunning = False
        
        for object in objects:
            object.process()
        
        screen.blit(PlayerHPText, (10, 10))
        screen.blit(EnemyHPText, (580, 10))
    
        # for posTime in textPosAndTime[:]:
        #     if posTime[1] > currentTime:
        #         screen.blit(Run, Run.get_rect(center = posTime[0]))

        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    main(screen)


























































































































# d = int(input("Do you want to play?\n1. Yes\n2. No\n"))
# print("-----------------------------------")
# if (d == 1):
#     print("-----------------------------")
#     print("|\tLoading Game!\t    |")
#     print("-----------------------------")
#     sleep(3)
#     print("---------------------------------------")
#     print("\tWelcome To The Dungeon!")
#     print("---------------------------------------")
#     print("Important Note: All instructions must be given in numbers!")
#     print(f"You encountered a {eencountered}!")
#     while (True):
#         CritHit = PlayerDMG * (CritDMG / 100)
#         PlayerDMG = r.randint(20, 30)
#         EnemyDMG = r.randint(1, 15)
#         Chance100 = r.randint(1, 100)
#         a = int(input("What to do? (Write in numbers) \n1. Attack \n2. Drink a Potion \n3. Run \n"))
#         if (a == 1):
#             if (Chance100 <= crithit.perc):
#                 PlayerHP = PlayerHP - EnemyDMG
#                 aa.hp = aa.hp - int(CritHit)
#                 print("A critical hit!")
#                 print(f"You dealt {int(CritHit)} DMG to the {eencountered}! It now has {aa.hp} HP left!")
#                 print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
#                 if (PlayerHP <= 0 and aa.hp <= 0):
#                     print("\tYou are too weak to move on, so you escape!")
#                     break
#                 elif (PlayerHP <= 0):
#                     print("\tYou are too weak to move on, so you escape!")
#                     break
#                 elif (aa.hp <= 0):
#                     c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
#                     if (c == 1):
#                         Kills = Kills + 1
#                         if (Chance100 > healthpotion.perc):
#                             aa.hp = 70
#                             print(f"You encountered a {eencountered}!")
#                         elif (Chance100 <= healthpotion.perc):
#                             A.num = A.num + 1
#                             aa.hp = 70
#                             print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
#                             print(f"You encountered a {eencountered}!")
#                     else:
#                         # print("You left the dungeon, successful in your quest!")
#                         print("You got tried of these small-fry and hence, went away!")
#                         break
#             else:
#                     PlayerHP = PlayerHP - EnemyDMG
#                     aa.hp = aa.hp - PlayerDMG
#                     print(f"You dealt {PlayerDMG} DMG to the {eencountered}! It now has {aa.hp} HP left!")
#                     print(f"The {eencountered} retaliated, dealing {EnemyDMG} DMG to you! You now have {PlayerHP} HP left!")
#                     if (PlayerHP <= 0):
#                         print("\tYou are too weak to move on, so you escape!")
#                         break
#                     if (aa.hp <= 0):
#                         c = int(input("You defeated the enemy! What to do now?\n1. Continue\n2. Escape\n"))
#                         if (c == 1):
#                             Kills = Kills + 1
#                             if (Chance100 > healthpotion.perc):
#                                 aa.hp = 70
#                                 print(f"You encountered a {eencountered}!")
#                             elif (Chance100 <= healthpotion.perc):
#                                 A.num = A.num + 1
#                                 aa.hp = 70
#                                 print(f"The enemy dropped a Health Potion! You now have {A.num} Health Potions!")
#                                 print(f"You encountered a {eencountered}!")
#                         elif (c == 2):
#                             print("You left the dungeon, successful in your quest!")
#                             break
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#         elif (a == 2):
#                 for index, item in enumerate(bag, 1):
#                     print(f"{index}. {item}")
#                 b = input("Which potion to drink? ")
#                 if (b == "1"):
#                     if (A.num > 0):
#                         PlayerHP = PlayerHP + A.effect
#                         A.num = A.num - 1
#                         print(f"You drank a Health Potion! It healed you for 30 HP! You now have {PlayerHP} HP!")
#                         print(f"You now have {A.num} Health Potions left!")
#                     elif (A.num <= 0):
#                         print("You don't have any Health Potions left!")
#                 elif (b == "2"):
#                     pass
#                 #     if (SPots > 0):
#                 #         PlayerDMG = PlayerDMG + SPE
#                 #         SPots = SPots - 1
#                 #         print(f"You drank a Stength Potion! It increased your damage by 20 DMG!")
#                 #         print(f"You now have {SPots} Strength Potions left!")
#                 elif (b == "3"):
#                     pass
#                 elif (b == "4"):
#                     pass
#                 elif (b == "5"):
#                     pass
#                 else:
#                     print("\tNot in the game yet!")
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#         else:
#             print("You ran away in fear!")
#             break