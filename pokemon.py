import random

#Create New Pokemon
class Pokemon:
    def __init__(self, name, elem_type, max_health, attacks):
        self.name = name
        self.elem_type = elem_type
        self.max_health = max_health
        self.attacks = attacks
        self.awake = True
        self.current_health = max_health
        self.attack_name = []
        self.attack_strength = []
        self.heal_name = []
        self.heal_strength = []

    #Stat read out
    def stat_read(self):
        temp_stats = {
            "Name": self.name,
            "Type": self.elem_type,
            "Health": self.current_health
        }
        for value, key in temp_stats.items():
            print (value + " : " + str(key))
        print ("")
        move_index = 0
        for value, key in self.attacks.items():
            move_index += 1
            print ("{move}. {name} : {power} ({type})".format(move = move_index, name = value, power = key[0], type = key[1])) 

    #Prep pokemon for battle
    def battle_ready(self):
        for value, key in self.attacks.items():
            if key[1] == "Attack":
                self.attack_name.append(value)
                self.attack_strength.append(key[0]) #Bug occuring: Moves labeled "attack" are appended twice and the "Heal" moves are not.
            elif key[1] == "Heal":
                self.heal_name.append(value)
                self.heal_strength.append(key[0])

#Test Pokemon
ninetales = Pokemon("Ninetales", "fire", 73, {
    "Quick Attack": [20, "Attack"],
    "Ember": [25, "Attack"],
    "Fuel": [10, "Heal"]
    })
machamp = Pokemon("Machamp", "fighting", 90, {
    "Dynamic Punch": [30, "Attack"],
    "Vital Punch": [20,"Attack"],
    "Armor": [5, "Heal"]
    })

#Duke it out
class Battle:
    def __init__(self, poke_1, poke_2):
        self.poke_1 = poke_1
        self.poke_2 = poke_2
        self.poke_1.battle_ready()
        self.poke_2.battle_ready()
        self.turn_id = 0
        self.choice = 0
        self.comp_choice = 0

    #Read out for each user turn
    def read_out(self):
        print ("YOUR POKEMON")
        self.poke_1.stat_read()
        print ("")
        print ("OPPOSING POKEMON:")
        self.poke_2.stat_read()

    #Prompt user move
    def user_move(self):
        self.choice = input("Please pick a move: ")
        return self.choice

    #Select random computer attack
    def comp_move(self):
        self.comp_choice = random.randint(1, 2)
        return self.comp_choice

    #Decide if attack is critical or not
    def is_critical(self):
        critical = False
        temp_rand = random.randint(1,4)
        if temp_rand == 4:
            critical = True
        else:
            critical = False
        return critical

    #Deal damage and read out attack info
    def attack(self):
        critical = self.is_critical()
        if self.turn_id % 2 != 0:   #user attack   
            try:
                choice_int = int(self.choice)
                if choice_int > 0 and choice_int <= 4:
                    hit = self.poke_1.attack_strength[choice_int - 1]
                    if critical == False:
                        self.poke_2.current_health -= hit
                        print ("You attacked with {name} for {damage} damage.".format(name = self.poke_1.attack_name[choice_int - 1], damage = hit))
                    elif critical == True:
                        crit_hit = hit * 1.3
                        self.poke_2.current_health -= crit_hit
                        print ("It's a critical attack!")
                        print ("You attacked with {name} for {damage} damage!".format(name = self.poke_1.attack_name[choice_int - 1], damage = crit_hit))
            except ValueError:
                print ("Please pick a valid attack. (1-4)")
        elif self.turn_id % 2 == 0:    #computer attack
            comp_choice_int = (self.comp_choice)
            comp_hit = self.poke_2.attack_strength[comp_choice_int - 1]
            if critical == False:
                self.poke_1.current_health -= comp_hit
                print ("You were attacked with {name} for {damage} damage.".format(name = self.poke_2.attack_name[comp_choice_int - 1], damage = comp_hit))
            elif critical == True:
                comp_crit_hit = comp_hit * 1.3
                self.poke_1.current_health -= comp_crit_hit
                print ("It's a critical attack!")
                print ("You were attacked with {name} for {damage} damage.".format(name = self.poke_2.attack_name[comp_choice_int - 1], damage = comp_crit_hit))

    #Knock out pokemon        
    def knock_out(self):
        if self.poke_1.current_health <= 0:
            self.poke_1.awake = False
            print (self.poke_1.name + " was knocked out by " + self.poke_2.name + ".")
        elif self.poke_2.current_health <= 0:
            self.poke_2.awake = False
            print (self.poke_2.name + " was knocked out by " + self.poke_1.name + ".")

    #User Turn
    def user_turn(self):
        while self.poke_1.current_health > 0 and self.poke_2.current_health > 0:
            self.turn_id += 1
            self.read_out()
            self.user_move()
            print ()
            self.attack()
            self.turn_id += 1
            print ()
            self.comp_move()
            self.attack()
            print ()
        self.knock_out()

#Run
test_battle = Battle(ninetales, machamp)
test_battle.user_turn()