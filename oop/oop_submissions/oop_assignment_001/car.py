class Car:
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0):
        if max_speed < 0:
            raise ValueError("Invalid value for max_speed")
        if acceleration < 0:
            raise ValueError("Invalid value for acceleration")
        if tyre_friction < 0:
            raise ValueError("Invalid value for tyre_friction")
       
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._current_speed = 0
        self._is_engine_started = False
                                                                                
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
    def current_speed(self):
        return self._current_speed
        
    @property
    def is_engine_started(self):
        return self._is_engine_started
    
        
        
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
        return self._is_engine_started
        
      
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
            return self._current_speed
        else:
            self._current_speed = 0
        
       
    def sound_horn(self):
        if self._is_engine_started:
            print("Beep Beep")
        else:
            print("Start the engine to sound_horn")
            
          
    def stop_engine(self):
         self._is_engine_started = False
         return self._is_engine_started
         
        
            
            
        
#car = Car("Red",-250,10,3)
#print(car._color)
#if self._acceleration > self._max_speed and self._max_speed > 0:
            #raise ValueError("Invalid value for acceleration")
        
            #raise ValueError("Invalid value for %d" % (self._acceleration))
        #if self._tyre_friction < 0:
         #   raise ValueError("Invalid value for tyre_friction")
        
            #raise ValueError("Invalid value for %d" % (self._tyre_friction))
        
