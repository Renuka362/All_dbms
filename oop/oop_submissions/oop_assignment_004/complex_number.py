class ComplexNumber:
    def __init__(self,real_part=0,imaginary_part=0):
        
        if type(real_part) == str and type(imaginary_part) == str:
            raise ValueError("Invalid value for real and imaginary part")
            
        if type(real_part) == str:
            raise ValueError("Invalid value for real part")
        else:    
            self.real_part = real_part
            
        if type(imaginary_part) == str:
            raise ValueError("Invalid value for imaginary part")
        else:
            self.imaginary_part = imaginary_part
        
    def __str__(self):
        return f'{self.real_part}{self.imaginary_part:+}i'
    
    def conjugate(self):
        return __class__(self.real_part,-self.imaginary_part)
        
    def __add__(self,other):
        return __class__(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)
        
    def __sub__(self,other):
        return __class__(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)
        
    def __mul__(self,other):
        return ComplexNumber(self.real_part*other.real_part-self.imaginary_part*other.imaginary_part,self.real_part*other.imaginary_part+self.imaginary_part*other.real_part)

    def __truediv__(self,other):
        s_real,s_imaginary,o_real,o_imaginary = self.real_part , self.imaginary_part ,other.real_part,other.imaginary_part
        k = float(o_real**2 + o_imaginary**2)
        v1 = ((s_real*o_real)+(s_imaginary*o_imaginary))/k
        v2 = ((s_imaginary*o_real)-(s_real*o_imaginary))/k
        return __class__(v1,v2)
        
    def __abs__(self):
        return round(((self.real_part**2+self.imaginary_part**2)**0.5),3)
        
    def __eq__(self,other):
        return bool(self.real_part==other.real_part and self.imaginary_part == other.imaginary_part)
        
       