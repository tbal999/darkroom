# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:22:28 2019

@author: thomas balcombe
"""
import random 
import time
from copy import copy
doublecheck = 0

class Map:
    global nest
    global level
    def __init__(self):
        self.area = []
        self.nest = []
        self.earea = []
        self.enest = []
    def Build(self, x, y):
        ycheck = 0
        xcheck = 0
        while ycheck < y:
            self.nest.append(0)
            ycheck = ycheck+1
        while xcheck < x:
            self.area.append(copy(self.nest))
            xcheck = xcheck+1
        self.earea.append(self.area)
        self.area[-1][0] = 9
        for i in self.area:
            print(i)
    def Clear(self):
        self.area = []
        self.nest = []
    def Print(self):
        for i in self.area:
            print(i)
    def GeneratePlayer(self):
        print("================")
        print("===DARK ROOM===")
        print("================")
        global hero
        hero = Character()
        print("new game...")
        hero.name = input("What is your character name? ")
        hero.health = random.randint(50,100)
        hero.attack = 1
        hero.equip = "bare fists"
        print(f"Good luck, {hero.name}.")
        print(f"Your currently can do {hero.attack} damage")
        print(f"Your HP is {hero.health}")
        print("Your current dungeon area is below")
    def GenerateMap(self, x):
        checker = -1 
        while checker <= x:
            try:
                checker = checker+1
                yc = random.randint(0,len(self.area))
                xc = random.randint(0,len(self.area[0]))
                #print(xc,yc)
                self.area[yc][xc] = 1
            except:
                self.area[-1][0] = 9
                #print(yc, xc, len(self.area),len(self.area[0]))
        #print(xc, yc, len(self.area),len(self.area[0]))
        self.area[-1][0] = 9
    def GenerateItems(self, x):
        checker = -1 
        while checker <= x:
            try:
                checker = checker+1
                yc = random.randint(0,len(self.area))
                xc = random.randint(0,len(self.area[0]))
                #print(xc,yc)
                self.area[yc][xc] = random.randint(2,8) 
            except:
                self.area[-1][0] = 9
                #print(yc, xc, len(self.area),len(self.area[0]))
        #print(xc, yc, len(self.area),len(self.area[0]))
        self.area[-1][0] = 9
    def GenerateEntity(self, x):
        checker = -1 
        while checker <= x:
            try:
                checker = checker+1
                yc = random.randint(0,len(self.area))
                xc = random.randint(0,len(self.area[0]))
                #print(xc,yc)
                self.area[yc][xc] = random.randint(10,12) 
            except:
                self.area[-1][0] = 9
                #print(yc, xc, len(self.area),len(self.area[0]))
        #print(xc, yc, len(self.area),len(self.area[0]))
        self.area[-1][0] = 9
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
        print("You go back.")
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
        global level
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex] != 9 and self.area[yindex][xindex] != 0:
                    return()
        print("You find a door that leads to another area...")
        newmap.Print()
        print("You successfully completed this floor.")
        print("You gained 2 points")
        print("You are now in another part of the dungeon...")
        time.sleep(2)
        newmap.Clear()
        newmap.Build(random.randint(2,5),random.randint(2,5))  
        newmap.GenerateMap(len(newmap.area)/4)
        newmap.GenerateItems(len(newmap.area)/3)
        newmap.GenerateEntity(len(newmap.area)/2)
        level = level+2
        game()
  
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
            print("You see a few rays of light from high above; asides that, there's nothing.")
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
        PickItem("sword")
        return()
    if x == 3:
        print("A shadow shoots at you, knocking you off your feet.")
        print("You drop your weapon.")
        hero.attack = 1
        print(f"You now have {hero.attack} attack")
        return()
    if x == 4:
        PickItem("shield")
        return()
    if x == 5:
        PickItem("templar mace")
        return()
    if x == 6:
        PickItem("dagger")
        return()
    if x == 7:
        PickItem("excalibur")
        return()
    if x == 7:
        PickItem("giant frying pan")
        return()
    if x == 10:
        print("You've found yourself a shadow beast")
        Fight("shadow beast")
        return()
    if x == 11:
        print("You've found yourself a small toad")
        Fight("toad")
        return()
    if x == 12:
        print("A goblin is alerted by your presence.")
        Fight("goblin")
        return()
        
def PickItem(x):
    global hero
    item = Item1.name.index(x)
    hero.attack = hero.attack + Item1.attack[item]
    hero.defense = hero.defense + Item1.defense[item]
    print(f"You picked up a {Item1.name[item]}")
    print(f"This gives you an extra {Item1.attack[item]} attack")
    print(f"This also gives you an extra {Item1.defense[item]} defense")
    return()

def Fight(x):
    global level
    global creature
    global doublecheck
    creature = Monster.name.index(x)
    print(f"There's a {Monster.name[creature]} ahead!")
    print(f"The {Monster.name[creature]} lunges at you...")
    creaturehealth = Monster.health[creature]
    creatureattack = Monster.attack[creature]
    while hero.health >= 0:
        hero.health = hero.health + (hero.defense-creatureattack)
        print(f"You take {hero.defense-Monster.attack[creature]} damage.")
        creaturehealth = creaturehealth - hero.attack
        print(f"You strike the {Monster.name[creature]} for {hero.attack} damage")
        healthcheck()
        if creaturehealth <= 0:
            doublecheck = 0
            level = level + 1
            print(f"You successfully killed the {Monster.name[creature]}.")
            print(f"You have {hero.health} hp remaining")
            return()
    print("You have died.")
    print(f"Your final score was {level}")
    print()
    doublecheck = 0
    time.sleep(2)
    start()

def healthcheck():
    global doublecheck
    if hero.health < 30 and doublecheck == 0:
        kk = input("You have dropped below 30 health, do you wish to continue fighting? [y] / [n]")
        if kk == 'y':
            doublecheck = 1
            return()
        if kk == 'n':
            print(f"You manage to run away from the {Monster.name[creature]}")
            doublecheck = 1
            game()
            
class Item:
  def __init__(self):
    self.name = []
    self.defense = []
    self.attack = []
  def BuildItem(self,a,b,c):
      self.name.append(a)
      self.defense.append(b)
      self.attack.append(c)
    
class Monsta:
  def __init__(self):
    self.name = []
    self.health = []
    self.defense = []
    self.attack = []
    self.score = []
  def BuildMonster(self,a,b,c,d,e):
      self.name.append(a)
      self.health.append(b)
      self.defense.append(c)
      self.attack.append(d)
      self.score = e

class Character:
  def __init__(self):
    self.name = ""
    self.health = 0
    self.defense = 0
    self.attack = 0
    self.equip = ""

def start():
    global newmap
    global Monster
    global Item1
    global level
    Monster = Monsta()
    Item1 = Item()
    Monster.BuildMonster("goblin",15,0,3,2)
    Monster.BuildMonster("toad",10,0,1,1)
    Monster.BuildMonster("shadow beast",20,0,5,3)
    Item1.BuildItem("sword",0,5)
    Item1.BuildItem("dagger",0,2)
    Item1.BuildItem("shield",2,0)
    Item1.BuildItem("templar mace",1,7)
    Item1.BuildItem("excalibur",5,10)
    Item1.BuildItem("giant frying pan",1,3)
    Item1.BuildItem("excalibur",5,10)
    newmap = Map()
    newmap.GeneratePlayer() 
    newmap.Build(random.randint(2,5),random.randint(2,5))   
    newmap.GenerateMap(2)
    newmap.GenerateItems(4)
    newmap.GenerateEntity(5)
    print("Your current score is 0. You gain points for killing monsters and completing levels.")
    print("You find yourself in a darkly lit room...")
    print()
    print("You can move forwards, backwards, left or right.")
    print("Controls: [w] - forwards, [s] - backwards, [a] - left, [d] - right.")
    print("Press anything else to quit, i.e 'quit'.")
    level = 0
    game()
                       
def game():
    global level
    global newmap
    print(f"Your current score is: {level}")
    x = input("Choose your option:" )
    print("Controls: [w] - forwards, [s] - backwards, [a] - left, [d] - right.")
    print("[p] - Player stats.")
    print("Press anything else to quit, i.e 'quit'.")
    print()
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
        print(f"Here are your stats, {hero.name}")
        print(f"Your health is: {hero.health}")
        print(f"You have {hero.attack} attack")
        print(f"You have {hero.defense} defense")
        game()
    else:
        quit()

start()
