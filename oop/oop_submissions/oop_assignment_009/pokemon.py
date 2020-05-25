class Pokemon:
    sound = ""
    running = ""
    def __init__(self,name,level=1):
        if name == "":
            raise ValueError("name cannot be empty")
        if level <=0:
            raise ValueError("level should be > 0")
        self._name = name
        self._level = level
        self._master = ""
        
        
    @property 
    def master(self):
        if self._master == "":
            print("No Master")
            
        else:
            return self._master
            
            
    @property 
    def name(self):
        return self._name
        
    @property 
    def level(self):
        return self._level
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    @classmethod
    def run(cls):
        if cls.running == "":
            print("Can not run")
        else:
            print(f'{cls.running} running...')
        
    def __str__(self):
        return f'{self._name} - Level {self._level}'
    
class Water_Pokemon:
    swim_obj = ""
    @classmethod
    def swim(cls):
        print(f'{cls.swim_obj} swimming...')
        
        
class Fly:
    fly_obj = ""
    @classmethod
    def fly(cls):
        print(f'{cls.fly_obj} flying...')
            
class Pikachu(Pokemon):
    sound = "Pika Pika"
   # running = "Pikachu"
    def attack(self):
        print(f'Electric attack with {10*self._level} damage')
        
            
class Squirtle(Pokemon,Water_Pokemon):
    sound = "Squirtle...Squirtle"
    running = "Squirtle"
    swim_obj = "Squirtle"
    
    def attack(self):
        print(f'Water attack with {9*self._level} damage')
        
 
class Pidgey(Pokemon,Fly):
    sound = "Pidgey...Pidgey"
    fly_obj = "Pidgey"
    def attack(self):
        print(f'Air attack with {5*self._level} damage')
        
class Swanna(Pokemon,Fly,Water_Pokemon):
    sound = "Swanna...Swanna"
    fly_obj = "Swanna"
    swim_obj = "Swanna"
    def attack(self):
        print(f'Water attack with {9*self._level} damage')
        print(f'Air attack with {5*self._level} damage')
       
class Zapdos(Pokemon,Fly):
    sound = "Zap...Zap"
    fly_obj = "Zapdos" 
    def attack(self):
        print(f'Electric attack with {10*self._level} damage')
        print(f'Air attack with {5*self._level} damage')
        
class Island:
    _island_list = []
    _pokemon_list = []
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name = name
        self._max_no_of_pokemon = max_no_of_pokemon
        self._total_food_available_in_kgs = total_food_available_in_kgs
        self._pokemon_left_to_catch = 0 
        self._island_list.append(self)
       
        
    @property     
    def name(self):
        return self._name
    
    @property 
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
        
    @property  
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs
        
    @property    
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch
        
    def __str__(self):
        return f'{self._name} - {self._pokemon_left_to_catch} pokemon - {self._total_food_available_in_kgs} food'
        
    def add_pokemon(self,pokemon):
        self._pokemon_list.append(pokemon)
        if self._pokemon_left_to_catch != self._max_no_of_pokemon:
            self._pokemon_left_to_catch += 1
        elif self._pokemon_left_to_catch == self._max_no_of_pokemon:
            print('Island at its max pokemon capacity')
            
    @classmethod        
    def get_all_islands(cls):
        return cls._island_list
        

class Trainer:
    _count = 0
    def __init__(self,name):
        self._name = name
        self._food_in_bag = 0
        self._current_island = None
        self._experience = 100
        self._max_food_in_bag = 10*self._experience
        self._pokemon_list = []
        
            
        
    def __str__(self):
        return f"{self._name}"
        
    @property 
    def name(self):
        return self._name
        
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
        
    @property 
    def experience(self):
        return self._experience
        
    @property
    def current_island(self):
        if self._current_island == None:
            print("You are not on any island")
        else:
            return self._current_island
            
    @property 
    def food_in_bag(self):
        return self._food_in_bag
    
        
    def move_to_island(self,island):
        self._current_island = island
        
        
    def collect_food(self):
        if self._current_island == None:
            print("Move to an island to collect food")
        
        else:
            if self._current_island._total_food_available_in_kgs > self._max_food_in_bag:
                if self._food_in_bag  < self._max_food_in_bag:
                    self._current_island._total_food_available_in_kgs -= self._max_food_in_bag
                    self._food_in_bag += self._max_food_in_bag
                
                else:
                    self._food_in_bag = self._max_food_in_bag
                
            else:
                self._food_in_bag = self._current_island.total_food_available_in_kgs
                self._current_island._total_food_available_in_kgs = 0
            
            
    def catch(self,pokemon):
        pokemon._master = self
        self._pokemon_list.append(pokemon)
        if self._experience >= (100*pokemon._level):
            self._experience += 20
            print(f'You caught {pokemon._name}')
        else:
            print(f'You need more experience to catch {pokemon._name}')
            
    def get_my_pokemon(self):
        return self._pokemon_list
            
                




























obj = Pikachu
obj.run()

        
"""    
if self._current_island not in self._island_list:
        
trainer = Trainer(name="Bot") 

print(pokemon._name)
#Pigetto
print(pokemon._level) 
#1
print(trainer._experience)

trainer.catch(pokemon)  # Print
#You caught Pigetto        
"""        
  
"""  
trainer = Trainer("Bot")
island1 = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
trainer.move_to_island(island1)
print(trainer.current_island == island1)
print(trainer.current_island)
#Island1 - 0 pokemon - 10000 - food
"""
        
"""
trainer = Trainer(name="Bot") 
print(trainer.name)
trainer = Trainer(name="Ryna") 
print(trainer.name)

"""

















        
        
"""      
island = Island(name="Island1", max_no_of_pokemon=100, total_food_available_in_kgs=10000)
island = Island(name="Island2", max_no_of_pokemon=24, total_food_available_in_kgs=12300)
island = Island(name="Island3", max_no_of_pokemon=82, total_food_available_in_kgs=11800)
island = Island(name="Island4", max_no_of_pokemon=192, total_food_available_in_kgs=101238)

Island.get_all_islands()
"""


"""
Island1 - 100 pokemon - 10000 food
Island2 - 24 pokemon - 12300 food
Island3 - 82 pokemon - 11830 food
Island4 - 192 pokemon - 101238 food 
""" 
""" 
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
island = Island(name="Island2", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
island = Island(name="Island8", max_no_of_pokemon=8, total_food_available_in_kgs=10000)
island = Island(name="Island6", max_no_of_pokemon=4, total_food_available_in_kgs=10000)
Island.get_all_islands()       
"""            
"""            
island = Island(name="Island1", max_no_of_pokemon=5, total_food_available_in_kgs=10000)
print(island._name)
print(island._max_no_of_pokemon)
print(island._total_food_available_in_kgs)
print(island._pokemon_left_to_catch)
print(island)
#Island1 - 0 pokemon - 10000 food     
#0
pokemon= Pikachu(name="Ryan", level=1)
island.add_pokemon(pokemon)
print(island._pokemon_left_to_catch)
#1
island._pokemon_left_to_catch  = 5

print(island._pokemon_left_to_catch)
#5
print(island._max_no_of_pokemon)
#5
island.add_pokemon(pokemon)  # Print
#Island at its max pokemon capacity
print(island._pokemon_left_to_catch)
#5
        
"""        
        
    
"""        
my_pikachu = Pikachu(name="Ryan", level=1)
print(my_pikachu.name)
print(my_pikachu)
my_pikachu.make_sound()  # Print
my_pikachu.run()  # Print
print(my_pikachu.level)
my_pikachu.attack()  # Print
another_pikachu = Pikachu(name="yan", level=2)
print(another_pikachu.level)
another_pikachu.attack() 
"""   
"""        
class Electric_Attack(Pokemon):
    mul_obj = ""
    def __init__(self,level):
        super().__init__(level)
            
    def attack(self):
        if (self._level%2) != 0:
            print(f'Electric attack with {self.mul_obj*self._level} damage')
        else:
            print(f'Electric Attack with {self.mul_obj*self._level} damage')
            
class Water_Attack(Pokemon):
    mul_obj = ""
    def __init__(self,level):
        super().__init__(level)
    def attack(self):
        if (self._level%2) != 0:
            print(f'Water attack with {self.mul_obj*self._level} damage')
        else:
            print(f'Water Attack with {self.mul_obj*self._level} damage')
"""            


    