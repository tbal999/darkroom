# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:22:28 2019

@author: thoma
"""
import random 
import time

class Map:
    def __init__(self):
        self.area = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    def Clear(self):
        self.area = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    def Print(self):
        for i in self.area:
            print(i)
    def GeneratePlayer(self):
        print("================")
        print("===DARK ROOM===")
        print("================")
        global hero
        self.area[4][0] = 9
        hero = Character("",0,0,0,0)
        print("new game...")
        hero.name = input("What is your character name? ")
        hero.health = random.randint(50,100)
        hero.attack = 1
        hero.equip = "bare fists"
        print(f"Ok, your character name is {hero.name}")
        print(f"Your currently can do {hero.attack} damage")
        print(f"Your HP is {hero.health}")
    def GenerateMap(self, x):
        checker = -1 
        while checker <= x:
            checker = checker+1
            for yindex, i in enumerate(self.area):
                xc = random.randint(0,4)
                yc = random.randint(0,4)
                if yindex == yc:
                    for xindex, i in enumerate(self.area):
                        if xindex == xc:
                            self.area[yindex][xindex] = 1
        self.area[4][0] = 9
    def GenerateItems(self, x):
        checker = -1 
        while checker <= x:
            checker = checker+1
            for yindex, i in enumerate(self.area):
                xc = random.randint(0,4)
                yc = random.randint(0,4)
                if yindex == yc:
                    for xindex, i in enumerate(self.area):
                        if xindex == xc:
                            self.area[yindex][xindex] = random.randint(2,5) 
        self.area[4][0] = 9
    def GenerateEntity(self, x):
        checker = -1 
        while checker <= x:
            checker = checker+1
            for yindex, i in enumerate(self.area):
                xc = random.randint(0,4)
                yc = random.randint(0,4)
                if yindex == yc:
                    for xindex, i in enumerate(self.area):
                        if xindex == xc:
                            self.area[yindex][xindex] = random.randint(6,6) 
        self.area[4][0] = 9
    def MoveUp(self):
        print("You press on forwards into the unknown.")
        self.IsGameOver()
        time.sleep(1)
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex] == 9:
                    if self.area[yindex-1][xindex] != 0:
                        checkNumber(self.area[yindex-1][xindex])
                        self.area[yindex-1][xindex] = 9
                        self.area[yindex][xindex] = 0
                        return()
                    self.area[yindex][xindex] = 0
                    self.area[yindex-1][xindex] = 9
                    return()
        self.Print()
    def MoveDown(self):
        print("You turn around and walk backwards, noticing your path has changed from what it was before.")
        self.IsGameOver()
        time.sleep(1)
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex-1][xindex] == 9:
                    if self.area[yindex][xindex] != 0:
                        checkNumber(self.area[yindex][xindex])
                        self.area[yindex][xindex] = 9
                        self.area[yindex-1][xindex] = 0
                        return()
                    self.area[yindex-1][xindex] = 0
                    self.area[yindex][xindex] = 9
                    return()
        self.Print()
    def MoveLeft(self):
        print("You take a left turn and move forwards")
        self.IsGameOver()
        time.sleep(1)
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex] == 9:
                    if self.area[yindex][xindex-1] != 0:
                        checkNumber(self.area[yindex][xindex-1])
                        self.area[yindex][xindex-1] = 9
                        self.area[yindex][xindex] = 0
                        return()
                    self.area[yindex][xindex-1] = 9
                    self.area[yindex][xindex] = 0
                    return()
        self.Print()
    def MoveRight(self):
        print("You take a right turn and move forwards")
        self.IsGameOver()
        time.sleep(1)
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex-1] == 9:
                    if self.area[yindex][xindex] != 0:
                        checkNumber(self.area[yindex][xindex])
                        self.area[yindex][xindex] = 9
                        self.area[yindex][xindex-1] = 0
                        return()
                    self.area[yindex][xindex] = 9
                    self.area[yindex][xindex-1] = 0
                    return()
    def IsGameOver(self):
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex] != 9 and self.area[yindex][xindex] != 0:
                    return()
        print("You find a door that leads to the outside. You have successfully escaped!")
        print("You win.")
        time.sleep(2)
        start()
  
def checkNumber(x):
    global hero
    global newmap
    if x == '0':
        xx = random.randint(1,5)
        if xx == 1:
            print("Nothing of interest here, at least, nothing that you can see.")
            return()
        if xx == 2:
            print("There's nothing here except the smell of damp and the sound of dripping water.")
            return()
        if xx == 2:
            print("It's pitch black, there's an ocassional thumping noise but that's it.")
            return()
        if xx == 3:
            print("There's nothing here.")
            return()
        if xx == 4:
            print("Thankfully, nothing.")
            return()
        if xx == 5:
            print("You see a few rays of light from high above, otherwise there's nothing.")
            return()
    if x == 1:
        print("You have found yourself a map!")
        newmap.Print()
        print("It's a strange bunch of numbers on a grid")
        print()
        time.sleep(1)
        print("You know, intuitively, that where the number 9 is on the list, that's where you were last standing")
        print("You also know that you are now standing where the number 1 is")
        print("The map suddenly sets itself alight and burns up!")
        return()
    if x == 2:
        print("You have found a sword.")
        hero.equip = "sword"
        hero.attack = 5
        print(f"You now have {hero.attack} attack")
        return()
    if x == 3:
        print("A shadow shoots at you, knocking you off your feet.")
        print("You drop your weapon.")
        hero.equip = "bare fists"
        hero.attack = 1
        print(f"You now have {hero.attack} attack")
        return()
    if x == 4:
        print("You have found a broken lid of an ancient beer cask.")
        print("It looks like it could be a makeshift shield")
        hero.defense = 2
        print(f"You now have {hero.defense} defense")
        return()
    if x == 4:
        print("A beam of radiant light suddenly hits you and elates your spirit")
        hero.health = hero.health + 50
        hero.defense = hero.defense + 2
        print(f"You now have {hero.defense} defense")
        return()
    if x > 5:
        print("You've found yourself a shadow beast")
        Fight()
        return()

def Fight():
    print("The shadow beast lunges at you...")
    shadowbeasthealth = 30
    while hero.health >= 0:
        hero.health = hero.health + (hero.defense-5)
        print(f"You take {hero.defense-5} damage.")
        shadowbeasthealth = shadowbeasthealth - hero.attack
        print(f"You strike the shadow beast")
        if shadowbeasthealth <= 0:
            print("You successfully killed the shadow beast.")
            print(f"You have {hero.health} hp remaining")
            return()
    print("You have died.")
    time.sleep(2)
    start()
    
class Character:
  def __init__(self, name, health, attack, equip, defense):
    self.name = name
    self.health = health
    self.defense = defense
    self.attack = attack
    self.equip = equip

def start():
    global newmap
    newmap = Map()
    newmap.GeneratePlayer()    
    newmap.GenerateMap(1)
    newmap.GenerateItems(2)
    newmap.GenerateEntity(2)
    print("You find yourself in a darkly lit corridor. You're not sure how you got here! But you know you must press on.")
    print()
    print("You can move forwards, backwards, left or right.")
    print("Controls: [w] - forwards, [s] - backwards, [a] - left, [d] - right.")
    print("Press anything else to quit, i.e 'quit'.")
    game()
                       
def game():
    global newmap
    x = input("Choose your option:" )
    print("Controls: [w] - forwards, [s] - backwards, [a] - left, [d] - right.")
    print("Press anything else to quit, i.e 'quit'.")
    if x == "s":
        newmap.MoveDown()
        game()
    if x == "w":
        newmap.MoveUp()
        game()
    if x == "a":
        newmap.MoveLeft()
        game()
    if x == "d":
        newmap.MoveRight()
        game()
    if x == "p":
        newmap.Print()
        game()
    else:
        quit()

start()
