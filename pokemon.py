import random

#Create New Pokemon
class Pokemon:
    def __init__(self, name, elem_type, max_health, attacks):
        self.name = name
        self.elem_type = elem_type
        self.max_health = max_health
        self.attacks = attacks
        self.current_health = max_health
        self.attack_name = []
        self.attack_strength = []

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
        att_index = 0
        for value, key in self.attacks.items():
            att_index += 1
            print (str(att_index) + ". " + value + " : " + str(key))

    #Prep pokemon for battle
    def battle_ready(self):
        for value, key in self.attacks.items():
            self.attack_name.append(value)
            self.attack_strength.append(key)

#Test Pokemon
ninetales = Pokemon("Ninetales", "fire", 73, {"Ember": 20, "Quick Attack": 20})
machamp = Pokemon("Machamp", "fighting", 90, {"Dynamic Punch": 30, "Vital Punch": 20})

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
        self.choice = input("Please pick an attack: ")
        return self.choice

    #Select random computer attack
    def comp_move(self):
        self.comp_choice = random.randint(1, 2)
        return self.comp_choice

    #Deal damage and attack read out
    def attack(self):
        if self.turn_id % 2 != 0:      
            try:
                choice_int = int(self.choice)
                if choice_int > 0 and choice_int <= 4:
                    self.poke_2.current_health -= self.poke_1.attack_strength[choice_int - 1]
                    print ("You attacked with {name} for {damage} damage.".format(name = self.poke_1.attack_name[choice_int - 1], damage = self.poke_1.attack_strength[choice_int - 1]))
            except ValueError:
                print ("Please pick a valid attack. (1-4)")
        elif self.turn_id % 2 == 0:
            comp_choice_int = (self.comp_choice)
            self.poke_1.current_health -= self.poke_2.attack_strength[comp_choice_int - 1]
            print ("You were attacked with {name} for {damage} damage.".format(name = self.poke_2.attack_name[comp_choice_int - 1], damage = self.poke_2.attack_strength[comp_choice_int - 1])) 

    #User Turn
    def user_turn(self):
        while self.poke_1.current_health > 0 and self.poke_2.current_health > 0:
            self.turn_id += 1
            print (self.turn_id)
            self.read_out()
            self.user_move()
            print ()
            self.attack()
            self.turn_id += 1
            print ()
            print (self.turn_id)
            self.comp_move()
            self.attack()
            print ()


#Run
test_battle = Battle(ninetales, machamp)
test_battle.user_turn()