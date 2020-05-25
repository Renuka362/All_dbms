class Zoo:
    
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
     
       
    def count_animals(self):
        return len(self.animals)
        
    def feed(self,obj=None):
        if self._reserved_food_in_kgs >= obj.required_food_in_kgs:
            self._reserved_food_in_kgs -= obj.required_food_in_kgs
            obj.grow()
        
        
    
class Deer(Zoo):
    deer_count = 0
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
            
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        self.deer_count += 1
    
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
        
    @classmethod   
    def make_sound(cls):
        print("Buck Buck")
    
    @classmethod    
    def breathe(cls):
        print("Breathe in air")
        
class Lion(Zoo):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
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
        
        
    def grow(self):
        
        self._age_in_months += 1
        self._required_food_in_kgs += 4
    
    @classmethod    
    def make_sound(cls):
        print("Roar Roar")
    
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
    def hunt(self,)
        
        
class Shark(Zoo):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
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
    
        
    def grow(self):
        
        self._age_in_months += 1
        self._required_food_in_kgs += 8
        
    @classmethod    
    def make_sound(cls):
        print("Shark Sound")
    
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
    def hunt(self,zoo):
        if GoldFish.gold_fish_count > 0:
            GoldFish.gold_fish_count -= 1
            
        elif GoldFish.gold_fish_count == 0:
            print("No GoldFish to hunt")
        
        
        
class GoldFish(Zoo):
    gold_fish_count = 0
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
        if age_in_months > 1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        self.gold_fish_count += 1
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
        
    def grow(self):
        
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2
    
    @classmethod    
    def make_sound(cls):
        print("Hum Hum")
    
    @classmethod
    def breathe(cls):
        print("Breathe oxygen from water")
        
class Snake(Zoo):
    def __init__(self,age_in_months=0,breed=None,required_food_in_kgs=0):
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
        
        
    def grow(self):
        
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
    
    @classmethod    
    def make_sound(cls):
        print("Hiss Hiss")
    
    @classmethod
    def breathe(cls):
        print("Breathe in air")
        
    def hunt(self,zoo):
        if Deer.deer_count > 0:
            Deer.deer_count -= 1
            
        elif Deer.deer_count == 0:
            print("No deers to hunt")
        
        
"""     
deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
deer.grow()
print(deer.make_sound())
deer = Deer(age_in_months=1, breed="ELP", required_food_in_kgs=10)
deer.grow()
print(deer.required_food_in_kgs)
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
lion.grow()
print(lion.age_in_months)

zoo = Zoo()
print(zoo.reserved_food_in_kgs)
lion.hunt(zoo)
print(count.animals())
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)

zoo.feed(gold_fish)
print(zoo.reserved_food_in_kgs)
print(gold_fish.age_in_months)     
if Deer.deer_count > 0:
            Deer.deer_count -= 1
            self.animals.remove(zoo.breed)
            
        elif Deer.deer_count == 0:
            print("No deers to hunt")
       
"""


