
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
        return dmg

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        #base attack -> subclasses will override
        pass


class Warrior(Character):
    def __init__(self, name, health, attack_power, defense, speed):
        super().__init__(name, health, attack_power, defense, speed)
        self.rage = 0


    def attack(self, target):
        #check berserk, then apply the damage formula
        pass

class Mage(Character):
    def __init__(self, name, health, attack_power, defense, speed, mana):
        super().__init__(name, health, attack_power, defense, speed)
        self.mana = mana


    def attack(self, target):
        #fireball, costs aman to deal damge 1.5 * attackPower aapprox.
        #backlash also harma the mage slightly
        damageDealt = self.attack
        if self.mana > 50:
            damageDealt =  1.5 * self.attack
            #causes a little self damage

            dmgTaken = self.take_damage(10)
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


    def startBattle():
        warrior = Warrior("AmyWarrior", 130, 22, 12, 6)
        mage = Mage("SibaMage", 90, 30, 5, 8, 100)
        archer = Archer("IvyArcher", 100, 24, 7, 12, 0.30)


        turns = {"warrior" : warrior.speed, "mage":mage.speed, "archer":archer.speed}
        sortedTurns = {key: value for key, value in sorted(turns.items(), key = lambda item: item[1], reverse=True)}
        print(sortedTurns)
        cur = archer
        opponent = mage
        winner = False
        while not winner:            
            #winner = True

            #for player in sortedTurns:
                #two players
            
            #cur = sortedTurns[0]
            #opponent = sortedTurns[1]

            if cur.name == "archer":                
                dmgDealt = archer.attack(opponent)
                opponent.take_damage(dmgDealt)
                cur = opponent
                opponent = archer
            elif cur.name == "mage":
                dmgDealt  = mage.attack(opponent)
                opponent.take_damage(dmgDealt)
                
                cur = opponent
                opponent = mage

            elif cur.name == "warrior":
                dmgDealt = warrior.attack(opponent)
                opponent.take_damage()
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


    






Stimulator.startBattle()


