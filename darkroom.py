# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 15:22:28 2019

@author: thomas balcombe
"""
import random 
import time
from copy import copy
import sys
doublecheck = 0
mapsize = 2
difficulty = 0
level = 0

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
        self.area[-1][0] = 9
        for i in self.area:
            print(i)
        ycheck = 0
        xcheck = 0
        while ycheck < y:
            self.enest.append(0)
            ycheck = ycheck+1
        while xcheck < x:
            self.earea.append(copy(self.enest))
            xcheck = xcheck+1
        self.earea[-1][0] = 9
    def Clear(self):
        self.area = []
        self.nest = []
        self.earea = []
        self.enest = []
    def Print(self):
        for i in self.area:
            print(i)
    def GeneratePlayer(self):
        global hero
        logo()
        time.sleep(2)
        hero = Character()
        print("new game...")
        hero.name = input("What is your character name? ")
        hero.health = 100
        hero.attack = 2
        hero.equip = "bare fists"
        print(f"Good luck {hero.name}")
        time.sleep(0.5)
        print(f"Your currently can do {hero.attack} damage")
        print(f"Your HP is {hero.health}")
        time.sleep(0.5)
        print("You are labelled on the map as the number '9'")
        time.sleep(0.5)
        print("Your current dungeon area is detailed below...")
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
        global difficulty
        checker = -1 
        while checker <= x:
            try:
                checker = checker+1
                yc = random.randint(0,len(self.area))
                xc = random.randint(0,len(self.area[0]))
                #print(xc,yc)
                self.area[yc][xc] = random.randint(2,(2+difficulty)) 
            except:
                self.area[-1][0] = 9
                #print(yc, xc, len(self.area),len(self.area[0]))
        #print(xc, yc, len(self.area),len(self.area[0]))
        self.area[-1][0] = 9
    def GenerateEntity(self, x):
        global difficulty
        checker = -1 
        while checker <= x:
            try:
                checker = checker+1
                yc = random.randint(0,len(self.area))
                xc = random.randint(0,len(self.area[0]))
                #print(xc,yc)
                self.area[yc][xc] = random.randint(10,(10+difficulty)) 
            except:
                self.area[-1][0] = 9
                #print(yc, xc, len(self.area),len(self.area[0]))
        #print(xc, yc, len(self.area),len(self.area[0]))
        self.area[-1][0] = 9
    def MoveUp(self):
        print("You press on forwards...")
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
    def MoveUp1(self):
        for yindex, i in enumerate(self.earea):
            for xindex, a in enumerate(i):
                if self.earea[yindex][xindex] == 9:
                    self.earea[yindex][xindex] = 0
                    self.earea[yindex-1][xindex] = 9
                    for i in self.earea:
                        print(i)
                    return()
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
    def MoveDown1(self):
        for yindex, i in enumerate(self.earea):
            for xindex, a in enumerate(i):
                if self.earea[yindex-1][xindex] == 9:
                    self.earea[yindex-1][xindex] = 0
                    self.earea[yindex][xindex] = 9
                    for i in self.earea:
                        print(i)
                    return()
    def MoveLeft(self):
        print("You move left...")
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
    def MoveLeft1(self):
        for yindex, i in enumerate(self.earea):
            for xindex, a in enumerate(i):
                if self.earea[yindex][xindex] == 9:
                    self.earea[yindex][xindex-1] = 9
                    self.earea[yindex][xindex] = 0
                    for i in self.earea:
                        print(i)
                    return()
    def MoveRight(self):
        print("You move right...")
        self.IsGameOver()
        time.sleep(1)
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex-1] == 9:
                    if self.area[yindex][xindex] != 0:
                        checkNumber(self.area[yindex][xindex])
                        self.area[yindex][xindex] = 9
                        self.area[yindex][xindex-1] = 0
                        break
                    self.area[yindex][xindex] = 9
                    self.area[yindex][xindex-1] = 0
                    return()
    def MoveRight1(self):
        for yindex, i in enumerate(self.earea):
            for xindex, a in enumerate(i):
                if self.earea[yindex][xindex-1] == 9:
                    self.earea[yindex][xindex] = 9
                    self.earea[yindex][xindex-1] = 0
                    for i in self.earea:
                        print(i)
                    return()
    def IsGameOver(self):
        global difficulty
        global healthgage
        global mapsize
        global level
        global hero
        for yindex, i in enumerate(self.area):
            for xindex, a in enumerate(i):
                if self.area[yindex][xindex] > 9 and self.area[yindex][xindex] != 13:
                    return()
        print("You suddenly find yourself phasing...")
        hole()
        print("...into the next area.")
        print("You gained 2 points")
        time.sleep(1)
        hero.attack = 1+(level)
        hero.health = hero.health+(level)
        print(f"Because of your current score: {level}, your attack is now {hero.attack}, and your health has increased to {hero.health}...")
        print("You are now in another part of the dungeon...")
        time.sleep(2)
        newmap.Clear()
        mapsize = mapsize+1
        level = level+2
        newmap.Build(random.randint(2,mapsize),random.randint(2,mapsize))
        Generator()
        game()
  
def checkNumber(x):
    nothings = ["Nothing of interest here, at least, nothing that you can see."
                ,"There's nothing here except the smell of damp and the sound of dripping water."
                ,"It's pitch black, there's an ocassional thumping noise but that's it."
                ,"There's nothing here."
                ,"Thankfully, nothing."
                ,"You see a few rays of light from high above; asides that, there's nothing."]
    global hero
    global newmap
    global level
    global doublecheck
    global difficulty
    if x == 0:
        print(nothings[random.randint(0,5)])
        return()
    if x == 1:
        print("You have found yourself a scrap of paper.")
        newmap.Print()
        print("It's a strange bunch of numbers?")
        print()
        time.sleep(1)
        print("It's a Map!")
        print("It reveals to you where all the different creatures and items are in the dungeon...")
        print("It states:")
        print("Evil creatures are 10 and above.")
        print("Useful items are 8 and below.")
        time.sleep(1)
        print("Good luck.")
        print("The map suddenly sets itself alight and burns up!")
        return()
    if x == 2:
        PickItem("sword")
        return()
    if x == 3:
        PickItem("giant frying pan")
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
    if x == 8:
        hero.health = hero.health+(10+level)
        print("You found some healing water")
        print(f"You have gained {10+level} health")
        return()
    if x == 10:
        print("You've found yourself a small toad")
        Fight("toad")
        return()
    if x == 11:
        print("A goblin is alerted by your presence.")
        Fight("goblin")
        return()
    if x == 12:
        print("A cinnibar moth beast descends from the ceiling...")
        Fight("cinnibar")
        return()
    if x == 13:
        print("The ghost of bad luck spooks you!")
        print("You've lost your weapon... and can't find it!")
        time.sleep(0.5)
        print("You slip and fall. Oh no!")
        print(f"Your head hits the ground first... you lose {difficulty+10} health.")
        hero.health = hero.health-(difficulty+10)
        if hero.health <= 0:
            print("Unfortunately, you also died.")
            print(f"Your final score is {level}")
            print()
            doublecheck = 0
            time.sleep(2)
            difficulty = 0
            level = 0
            start()
        hero.attack = 1
        return()
    if x == 14:
        print("You've found yourself a shadow beast")
        Fight("shadow beast")
        return()
    if x == 15:
        print("A hooded rogue is not pleased by your arrival.")
        Fight("hooded rogue")
        return()
    if x == 16:
        print("A hooded rogue is not pleased by your arrival.")
        Fight("hooded rogue")
        return()
    if x > 16:
        print("A demon appears.")
        Fight("demon")
        return()

def logo():
    print("""
 ______   _______  ______    ___   _          
|      | |   _   ||    _ |  |   | | |         
|  _    ||  |_|  ||   | ||  |   |_| |         
| | |   ||       ||   |_||_ |      _|         
| |_|   ||       ||    __  ||     |_          
|       ||   _   ||   |  | ||    _  |         
|______| |__| |__||___|  |_||___| |_|         
 ______    _______  _______  __   __  _______ 
|    _ |  |       ||       ||  |_|  ||       |
|   | ||  |   _   ||   _   ||       ||  _____|
|   |_||_ |  | |  ||  | |  ||       || |_____ 
|    __  ||  |_|  ||  |_|  ||       ||_____  |
|   |  | ||       ||       || ||_|| | _____| |
|___|  |_||_______||_______||_|   |_||_______|

              """)
    return()

def hole():
    print("""

  |                    _,.-----.,_         o    |          
           +    *    .-'.         .'-.          -O-         
     *            .'.-'   .---.   `'.'.         |     *    
.                /_.-'   /     \   .'-.\                   
        ' -=*<  |-._.-  |       |   '-._|  >*=-    .     + 
-- )--           \`-.    \     /    .-'/                   
      *     +     `.'.    '---'    .'.'    +       o       
                 .  '-._         _.-'  .                   
         |               `~~~~~~~`       - --===D       @   
""")
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
    global difficulty
    creature = Monster.name.index(x)
    print(f"There's a {Monster.name[creature]} ahead!")
    print(f"The {Monster.name[creature]} lunges at you...")
    creaturehealth = Monster.health[creature] + difficulty
    creatureattack = Monster.attack[creature] + difficulty
    while hero.health >= 0:
        creaturehealth = creaturehealth - (hero.attack + hero.defense)
        print(f"You strike the {Monster.name[creature]} for {hero.attack} damage")
        healthcheck()
        if creaturehealth <= 0:
            doublecheck = 0
            level = level + 1
            print(f"You successfully killed the {Monster.name[creature]}.")
            print(f"You have {hero.health} health remaining.")
            if hero.health <= 0:
                print("Unfortunately, you also died.")
                print(f"Your final score is {level}")
                print()
                doublecheck = 0
                time.sleep(2)
                start()
            return()
        hero.health = hero.health - creatureattack
        print(f"You take {hero.defense-Monster.attack[creature]} damage.")
    print("You have died.")
    print(f"Your final score is {level}")
    print()
    doublecheck = 0
    difficulty = 0
    level = 0
    time.sleep(2)
    start()

def healthcheck():
    global doublecheck
    if hero.health < 30 and doublecheck == 0:
        kk = input("You have dropped below 30 health, do you wish to continue fighting? [y] / [n] ")
        print("If you choose to run away, you will retreat back to the previous point")
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

def Generator():
    global newmap
    global difficulty
    difficulty = difficulty + 1
    mapwidth = len(newmap.area[0])
    mapheight = len(newmap.area)
    print(mapwidth, mapheight)
    newmap.GenerateMap(1)
    newmap.GenerateItems(difficulty+1)
    newmap.GenerateEntity(difficulty)
    return()

def start():
    global newmap
    global Monster
    global Item1
    global level
    global difficulty
    Monster = Monsta()
    Item1 = Item()
    Monster.BuildMonster("goblin",15,0,2,2)
    Monster.BuildMonster("toad",10,0,1,1)
    Monster.BuildMonster("shadow beast",20,0,3,3)
    Monster.BuildMonster("hooded rogue",20,0,10,3)
    Monster.BuildMonster("cinnibar",40,0,1,1)
    Monster.BuildMonster("demon",30,0,12,1)
    Item1.BuildItem("sword",0,5)
    Item1.BuildItem("dagger",0,2)
    Item1.BuildItem("shield",2,0)
    Item1.BuildItem("templar mace",1,7)
    Item1.BuildItem("excalibur",5,10)
    Item1.BuildItem("giant frying pan",1,3)
    Item1.BuildItem("excalibur Xtreme",10,10)
    newmap = Map()
    newmap.Clear()
    newmap.GeneratePlayer() 
    newmap.Build(2,3)
    Generator()
    print("Your current score is 0. You gain points for killing monsters and completing levels.")
    print("If you successfully kill all monsters in a map, you will move to the next level")
    print("Every level will increase the difficulty")
    print("You find yourself in a darkly lit room...")
    print("===CONTROLS===")
    print("You can move forwards, backwards, left or right.")
    print("Controls: [w] - forwards, [s] - backwards, [a] - left, [d] - right.")
    print("[p] - Player stats.")
    print("Type q to quit if you want to.")
    print()
    level = 0
    game()
                       
def game():
    global level
    global newmap
    global difficulty
    print(f"Difficulty level: {difficulty}")
    print(f"Your current score is: {level}")
    x = input("Choose your option:" )
    try:
        if x == "s":
            newmap.MoveDown()
            newmap.MoveDown1()
            game()
        if x == "w":
            newmap.MoveUp()
            newmap.MoveUp1()
            game()
        if x == "a":
            newmap.MoveLeft()
            newmap.MoveLeft1()
            game()
        if x == "d":
            newmap.MoveRight()
            newmap.MoveRight1()
            game()
        if x == "p":
            print(f"Here are your stats, {hero.name}")
            print(f"Your health is: {hero.health}")
            print(f"You have {hero.attack} attack")
            print(f"You have {hero.defense} defense")
            game()
        if x == "q":
            quit()
            sys.exit()
        else:
            game()
    except:
        quit()

start()
