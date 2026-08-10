
import random


class Character:
    def __init__(self, name, health, attack_power, defense, speed):
        self.name = name
        self.health = health
        self.max_health = health   #starting health
        self.attack_power = attack_power
        self.defense = defense
        self.speed = speed

    def take_damage(self, amount):
        dmg = max(1, amount - self.defense)
        self.health -= dmg

        if isinstance(self, Warrior):
            #rage attribute
            self.rage += 10
            if self.health < (0.30 * self.max_health):
                self.attack_power = self.attack_power * 2
                print(self.name, "(Warrior) enters Berserk Mode! Attack power increased.")
            
        return dmg

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        #base attack -> subclasses will override
        pass


class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed, rage):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = rage


    def attack(self, target):
        #check berserk, then apply the damage formula
        damageDealt = self.attack_power
        if self.health < (0.30 * self.max_health):
            #self.attack_power = self.attack_power * 2
            #damageDealt = self.attack_power
            print(self.name, "(Warrior's) strikes with double power! Deals",{damageDealt}, "damage.")
        else:
            print(self.name, "(Warrior) swings a sword! Deals", damageDealt, "damage.")

        return damageDealt
        

class Mage(Character):
    def __init__(self, name, health, attack_power, defense, speed, mana):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = mana


    def attack(self, target):
        #fireball, costs aman to deal damge 1.5 * attackPower aapprox.
        #backlash also harma the mage slightly
        damageDealt = self.attack
        if self.mana > 50:
            damageDealt =  1.5 * self.attack_power
            #causes a little self damage

            dmgTaken = self.take_damage(10)
            #decrease mana
            self.mana -= 10
            print(self.name, "(Mage) casts Fireball! Deals", damageDealt, "damage but loses ",dmgTaken, "health.")

        else:
            print(self.name, "(Mage) casts a spell! Deals", damageDealt)

        return damageDealt



class Archer(Character):
    def __init__(self, name, health, attack_power, defense, speed, critical_chance):
        super().__init__(name, health, attack_power, defense, speed)
        self.critical_chance = critical_chance

    def attack(self, target):
        #on each attackt ehre is a 30% chance use random
        #to land a critical hit
        #that deals 2x damage
        #Announce distinctly in the log
        critcalHit = random.random() < 0.30
        print("Critical Hit: ", critcalHit)
        damageDealt = self.attack_power
        if critcalHit:
            damageDealt = 2 * self.attack_power

            print(self.name, "(Archer) lands a Critical Hit! Deals",{damageDealt}, "damage.")
        else:
            print(self.name, "(Archer) shoots an arrow! Deals", {damageDealt}, "damage.")

        return damageDealt

        
        




class Stimulator:
    def __init__(self):
        self.turn = ""
        self.hashMap = {}

    def createCharacter(self, characterType):
        hashMap = { 1: "Warrior", 2: "Mage", 3:"Archer"}

        #name, health, attack_power, defense, speed
        name = input("Enter name for character")
        health = float(input("Enter health for character"))
        attack_power = float(input("Enter attack power for character"))
        defense = float(input("Enter defense for character"))
        speed = float(input("Enter speed for character"))

        character = None
        if characterType == 1:
            rage = float(input("Enter rage value for your Warrior"))
            character = Warrior(name, health, attack_power, defense, speed, rage)

        elif characterType == 2:
            mana = float(input("Enter mana for your Mage"))
            character = Mage(name, health, attack_power, defense, speed, mana)
        elif characterType == 3:
            critical_chance = float(input("Enter critical chance probabilty for your Archer"))
            character = Archer(name, health, attack_power, defense, speed, critical_chance)
        print(character.name)
        return character
            




    def startBattle(self):
        warrior = Warrior("AmyWarrior", 130, 22, 12, 6, 0)
        mage = Mage("SibaMage", 90, 30, 5, 8, 100)
        archer = Archer("IvyArcher", 100, 24, 7, 12, 0.30)

        p1_type = int(input("Please select a type and enter the number against it. 1. warrior 2.mage 3.archer"))
        p1 = self.createCharacter(p1_type)
        p2_type = int(input("Please select a type and enter the number against it. 1. warrior 2.mage 3.archer"))
        p2 = self.createCharacter(p2_type)




        #turns = {"p1" : p1.speed, "p2":p2.speed}
        #sortedTurns = {key: value for key, value in sorted(turns.items(), key = lambda item: item[1], reverse=True)}
        #sortedTurns = sorted(turns, key=turns.get, reverse=True)
        #print(sortedTurns)
        """  cur = archer
        opponent = mage """

        #cur = sortedTurns[0]
        #opponent = sortedTurns[1]


        players = [p1, p2]
        players.sort(key=lambda x: x.speed, reverse=True)

        cur = players[0]
        opponent = players[1]
        winner = False
        while not winner:            
         

            if isinstance(cur, Archer):                
                dmgDealt = archer.attack(opponent)
                opponent.take_damage(dmgDealt)
                cur = opponent
                opponent = archer
            elif isinstance(cur, Mage):
                dmgDealt  = mage.attack(opponent)
                opponent.take_damage(dmgDealt)
                
                cur = opponent
                opponent = mage

            elif isinstance(cur, Warrior):
                dmgDealt = warrior.attack(opponent)
                opponent.take_damage(dmgDealt)
                cur = opponent
                opponent = warrior



            if opponent.health <= 0:
                print(opponent.name, "is deafeated!")
                print(cur.name, "wins the battle")
                winner = True

            else:
                print("Stats of current round")
                print(cur.name, "health stands at: ", cur.health)
                print(opponent.name, "health stands at: ", opponent.health)


    





s1 = Stimulator()

s1.startBattle()


