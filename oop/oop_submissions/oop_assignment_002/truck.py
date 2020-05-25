from car import Car
class Truck(Car):
    horn = "Honk Honk"
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._loads = 0
        
    @property    
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    @property 
    def loads(self):
        return self._loads
        
        
    def load(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
            
        if self._current_speed != 0:
            print("Cannot load cargo during motion")
            
        else:
            if self._loads+cargo_weight < self._max_cargo_weight:
                self._loads += cargo_weight
            else:
                print("Cannot load cargo more than max limit: " f'{self._max_cargo_weight}')
                
        
    def unload(self,cargo_weight):
        
            
        if self._current_speed != 0:
            print("Cannot unload cargo during motion")
            
        
        else:    
            self._loads -= cargo_weight
            
         
                       
       
    
        
"""
class Truck:
    
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._loads = 0
        self._current_speed = 0
        self._is_engine_started = False
        self._max_cargo_weight = max_cargo_weight
        if self._max_speed < 0:
            raise ValueError("Invalid value for max_speed")
        if self._acceleration < 0:
            raise ValueError("Invalid value for acceleration")
        if self._tyre_friction < 0:
            raise ValueError("Invalid value for tyre_friction")
        if self._max_cargo_weight < 0:
            raise ValueError("Invalid value for max_cargo_weight")
                                                                                
    @property    
    def acceleration(self):
        return self._acceleration
    
    @property
    def  max_speed(self):
        return self._max_speed
        
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def color(self):
        return self._color
        
    @property
    def loads(self):
        return self._loads
        
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
    @property
    def current_speed(self):
        return self._current_speed
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
        

    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
                return self._current_speed
            else:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
       
        
       
        
    def start_engine(self):
        self._is_engine_started = True
        
    
    def load(self,cargo_weight):
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
            
        if self._current_speed != 0:
            print("Cannot load cargo during motion")
            
        else:
            if self._loads+cargo_weight < self._max_cargo_weight:
                self._loads += cargo_weight
            else:
                print("Cannot load cargo more than max limit: " f'{self._max_cargo_weight}')
                
        
    def unload(self,cargo_weight):
        
        
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
            
        elif self._current_speed != 0:
            print("Cannot unload cargo during motion")
            
            
        else:
            self._loads -= cargo_weight
         
                       
       
    def sound_horn(self):
        if self._is_engine_started:
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
            
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
            return self._current_speed
        else:
            self._current_speed = 0
            
            
          
    def stop_engine(self):
         self._is_engine_started = False
         
  """
  
            
            
        
