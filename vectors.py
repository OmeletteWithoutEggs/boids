import math
import numpy as np

class Vector2():

    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    #addition
    def __add__(self,other):
        if isinstance(other,Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other,(list,tuple,np.ndarray)):
            return Vector2(self.x + other[0], self.y + other[1])
        else:
            return Vector2(self.x + other, self.y + other)
        
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self,other):
        if isinstance(other,Vector2):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other,(list,tuple,np.ndarray)):
            self.x += other[0]
            self.y += other[1]
            return self
        else:
            self.x += other
            self.y += other
            return self
        
    #subtraction 
    def __sub__(self,other):
        if isinstance(other,Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other,(list,tuple,np.ndarray)):
            return Vector2(self.x - other[0], self.y - other[1])
        else:
            return Vector2(self.x - other, self.y - other)
    
    def __rsub__(self, other):
        if isinstance(other,Vector2):
            return Vector2(other.x - self.x, other.y - self.y)
        elif isinstance(other,(list,tuple,np.ndarray)):
            return Vector2(other[0] - self.x, other[1] - self.y)
        else:
            return Vector2(self.x - other, self.y - other)
        
    
    def __isub__(self,other):
        if isinstance(other,Vector2):
            self.x -= other.x
            self.y -= other.y
            return self
        elif isinstance(other,(list,tuple,np.ndarray)):
            self.x -= other[0]
            self.y -= other[1]
            return self
            
        else:
            self.x -= other
            self.y -= other
            return self

    #multiplication
    def __mul__(self,other):
        if isinstance(other,Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other,(list,tuple)):
            return Vector2(self.x * other[0], self.y * other[1])
        else:
            return Vector2(self.x * other, self.y * other)
        
    
    def __rmul__(self,other):
        return self.__mul__(other)
        
    def __imul__(self,other):
        if isinstance(other,Vector2):
            self.x *= other.x
            self.y *= other.y
            return self
        elif isinstance(other,(list,tuple,np.ndarray)):
            self.x *= other[0]
            self.y *= other[1]
            return self
            
        else:
            self.x *= other
            self.y *= other
            return self


    #division
    def __truediv__(self,other):
        otherType = type(other)
        if type(other) == Vector2:
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(otherType,(list,tuple)):
            return Vector2(self.x/other[0],self.y/other[1])
        else:
            return Vector2(self.x / other, self.y / other)
        

    def __repr__(self):
        return f"{self.x},{self.y}"

    def abs(self):
        return Vector2(abs(self.x), abs(self.y))

    def floor(self):
        return Vector2(math.floor(self.x),math.floor(self.y))
    def ceil(self):
        return Vector2(math.ceil(self.x),math.ceil(self.y))
    
    def rounded(self,ndigits=0):
        return Vector2(round(self.x,ndigits),round(self.y,ndigits))



    #vector specifics
    def tupl(self):
        return (self.x, self.y)
    
    def integer(self):
        return Vector2(int(self.x),int(self.y))

    def magnitude(self):
        return math.hypot(self.x,self.y )
    
    def lengthSquared(self):
        return self.x **2 + self.y**2

  
    def normalise(self):
        try:
            length = self.magnitude()
            self.x /= length
            self.y /= length
        except:
            self.x = 0
            self.y = 0
    
    def setMagnitude(self, length):
        
        self.normalise()
        self *= length


    def limit(self,length):
        if self.magnitude()> length:
            self.normalise()
            self *= length

    def angle(self):
        """returns radians"""
        return math.atan2(self.y, self.x)
    
    def copy(self):
        return Vector2(self.x, self.y)
    
    def dot(self,other):
        return (self.x*other.x) + (self.y*other.y)
    
    def constrain(self, length):
        
        self.normalise()
        self * length

def normalised(vec):
    try:
        return Vector2(vec.x / vec.magnitude() , vec.y / vec.magnitude())
    except:
        return Vector2(0,0)



class Vector3():

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    #addition
    def __add__(self,other):
        if isinstance(other,Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other,(list,tuple,np.ndarray)):
            return Vector3(self.x + other[0], self.y + other[1], self.z + other[2])
        else:
            return Vector3(self.x + other, self.y + other, self.z + other)
        
    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self,other):
        return self.__add__(other)
        
    #subtraction 
    def __sub__(self,other):
        if isinstance(other,Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other,(list,tuple,np.ndarray)):
            return Vector3(self.x - other[0], self.y - other[1], self.z - other[2])
        else:
            return Vector3(self.x - other, self.y - other, self.z - other)
    
    def __rsub__(self, other):
        return self.__sub__(other)
    
    def __isub__(self,other):
        return self.__sub__(other)

    #multiplication
    def __mul__(self,other):
        otherType = type(other)
        if otherType == Vector3:
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(otherType,(list,tuple)):
            return Vector3(self.x * other[0], self.y * other[1], self.z * other[2])
        else:
            return Vector3(self.x * other, self.y * other, self.z * other)
        
    
    def __rmul__(self,other):
        return self.__mul__(other)
        
    def __imul__(self,other):
        return self.__mul__(other)

    #division
    def __truediv__(self,other):
        otherType = type(other)
        if otherType == Vector3:
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(otherType,(list,tuple)):
            return Vector3(self.x / other[0], self.y / other[1], self.z / other[2])
        else:
            return Vector3(self.x / other, self.y / other, self.z / other)
        

    def __repr__(self):
        return f"{self.x},{self.y},{self.z}"

    def abs(self):
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def floor(self):
        return Vector3(math.floor(self.x), math.floor(self.y), math.floor(self.z))
    def ceil(self):
        return Vector3(math.ceil(self.x), math.ceil(self.y), math.ceil(self.z))
    
    def rounded(self,ndigits=0):
        return Vector3(round(self.x, ndigits), round(self.y, ndigits), round(self.z, ndigits))



    #vector specifics
    def tupl(self):
        return (self.x, self.y, self.z)

    def magnitude(self):
        
        return math.sqrt((abs(self.x)**2) + (abs(self.y)**2) + (abs(self.z)**2))

    def normalised(self):
        try:
            mag = self.magnitude
            return Vector3(self.x / mag, self.y / mag, self.z / mag)
        except:
            return Vector3(0,0,0)
    def normalise(self):
        try:
            temp = self.magnitude()
            self.x /= temp
            self.y /= temp
            self.z /= temp
        except:
            pass
    
    def constrain(self, length):
        
        self.normalise()
        self *= length
        
        

    def angle(self):
        """returns radians"""
        return math.atan2(self.y, self.x)


def vector(target):
    if isinstance(target, (list,tuple)):
        if len(target) == 2:
            return Vector2(target[0], target[1])
        elif len(target) == 3:
            return Vector3(target[0], target[1], target[2])
    elif isinstance(target,(Vector2,Vector3)):
        return target

def tupl(obj):
    if isinstance(obj,Vector2):
        return (obj.x, obj.y)  
    elif isinstance(obj,Vector3):
        return (obj.x,obj.y,obj.z)
    