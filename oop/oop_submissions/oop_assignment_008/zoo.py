class Animal:
    sound = ""
    growth = 0
    def __init__(self,age_in_months,breed,required_food_in_kgs):
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.growth
        
        
class Land_Animal:
    @classmethod    
    def breathe(cls):
        print("Breathe in air")
        
    
class Water_Animal:
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")

class Hunting_Animal:
    def __init__(self):
        self.animal_obj = None
        self.animal_name = None
    def hunt(self,zoo_obj):
        for animal in zoo_obj.animals:
            if type(animal) == self.animal_obj:
                Zoo.total_animals.remove(animal)
                zoo_obj.animals.remove(animal)
                return
        print(f'No {self.animal_name} to hunt')
                
                
class Deer(Animal,Land_Animal):
    sound = "Buck Buck"
    growth = 2
    
class Lion(Animal,Land_Animal,Hunting_Animal):
    sound = "Roar Roar"
    growth = 4
    animal_obj = Deer
    animal_name = "deers"

class GoldFish(Animal,Water_Animal):
    sound = "Hum Hum"
    growth = 0.2
    
    
class Shark(Animal,Water_Animal,Hunting_Animal):
    sound = "Shark Sound"
    growth = 8
    animal_obj = GoldFish
    animal_name = "GoldFish"
    

class Snake(Animal,Land_Animal,Hunting_Animal):
    sound = "Hiss Hiss"
    growth = 0.5
    animal_obj = Deer
    animal_name = "deers"


    
    
    
class Zoo:
    total_animals = []
    def __init__(self):
        self._animals = []
        self._reserved_food_in_kgs = 0  
        
    
    @property 
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
        
    @property 
    def animals(self):
        return  self._animals
    
   
    def add_food_to_reserve(self,reserved_food_in_kgs):
        self._reserved_food_in_kgs = reserved_food_in_kgs
    
    def add_animal(self,obj=None):
        self.animals.append(obj)
        Zoo.total_animals.append(obj)
     
       
    def count_animals(self):
        return len(self.animals)
        
    def feed(self,obj=None):
        if self._reserved_food_in_kgs >= obj.required_food_in_kgs:
            self._reserved_food_in_kgs -= obj.required_food_in_kgs
            obj.grow()
            
    @classmethod
    def count_animals_in_all_zoos(cls):
        return len(Zoo.total_animals)
        
   
    @staticmethod
    def count_animals_in_given_zoos(zoo_list):
        count_of_each_zoo = 0
        count = 0
        for i in zoo_list:
            count_of_each_zoo = i.count_animals()
            count += count_of_each_zoo
        return count
"""        
zoo = Zoo()
d1 = Deer(1, 'elk', 2)
d2 = Deer(1, 'elk', 3)
d3 = Deer(1, 'renuka', 20)
lion = Lion(1, 'indian', 2)
#zoo.add_animal(d1)
#zoo.add_animal(d2)
#zoo.add_animal(d3)
zoo.add_animal(lion)
print(zoo.count_animals())
lion.hunt(zoo)
print(zoo.count_animals())
lion.hunt(zoo)
"""