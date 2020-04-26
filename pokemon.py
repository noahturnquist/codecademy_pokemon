#Create a Pokemon
class Pokemon:
    def __init__(self, name, level, poke_type, max_health, current_health, awake):
        self.name = name
        self.level = level
        self.poke_type = poke_type
        self.max_health = max_health
        self.current_health = current_health
        self.awake = awake

        self.stats = {
            "Name": self.name,
            "Level": self.level,
            "Type": self.poke_type,
            "Max Health": self.max_health,
            "Current Health": self.current_health,
            "Awake?": self.awake
        }
    #Print Pokemon Stats
    def read_stats(self):
        for value, key in self.stats.items():
            print (value + ": " + str(key))


#Player
class Player:
    def __init__(self):
        self.pokemon = {}

    def add_pokemon(self, new_pokemon):
        slot = 1
        for pair in self.pokemon:
            slot += 1
            return slot
        self.pokemon["Pokemon " + str(slot)] = new_pokemon

    def __repr__(self):
        return self.pokemon

#Player 1
player = Player()

#Starter Pokemon
bulbasaur = Pokemon("Bulbasaur", 1, "grass", 45, 45, True)
charmander = Pokemon("Charmander", 1, "fire", 39, 39, True)
squirtle = Pokemon("Squirtle", 1, "water", 44, 44, True)

#Play game
class Play:
    #Choose starter pokemon
    def start_game(self):
        print ("Welcome player. Please pick a number 1-3 to choose the cooresponding Pokemon as your starter.")
        print ("")
        print ("1.")
        bulbasaur.read_stats()
        print ("")
        print ("2.")
        charmander.read_stats()
        print ("")
        print ("3.")
        squirtle.read_stats()
        print ("")
        temp_choice = int(input("Choose your starter pokemon: "))
        if temp_choice == 1:
            player.pokemon["Pokemon 1"] = bulbasaur
        elif temp_choice == 2:
            player.pokemon["Pokemon 1"] = charmander
        elif temp_choice == 3:
            player.pokemon["Pokemon 1"] = squirtle
        print ("")
        print("You have choosen {pokemon}".format(pokemon = player.pokemon))

        

#Debug
#current_game = Play()
#current_game.start_game()
player.add_pokemon(charmander)
print (player.pokemon)