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

    #Read out for each user turn
    def read_out(self):
        print ("YOUR POKEMON")
        self.poke_1.stat_read()
        print ("")
        print ("OPPOSING POKEMON:")
        self.poke_2.stat_read()

    def attack(self):
        choice = int(input("Please pick an attack: "))
        if choice == 1:
            self.poke_2.current_health =- self.poke_1.attack_strength[choice - 1]
            print ("You attacked with {name} for {damage} damage.".format(name = self.poke_1.attack_name[choice - 1], damage = self.poke_1.attack_strength[choice - 1]))

     #User Turn
    def user_turn(self):
        print (self.poke_1.attack_strength[1])
        self.read_out()
        self.attack()

#Run
test_battle = Battle(ninetales, machamp)
test_battle.user_turn()