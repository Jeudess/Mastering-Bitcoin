class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:  
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num  
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    # Exercise 1.1
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __add__(self, other):
        if self.prime != other.prime:  
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime  
        return self.__class__(num, self.prime)
    
    # Exercise 1.3
    def __sub__(self,other):
        if self.prime != other.prime:  
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime  
        return self.__class__(num, self.prime)
    
    # Exercise 1.6
    def __mul__(self,other):
        if self.prime != other.prime:  
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime  
        return self.__class__(num, self.prime)

class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y

        if self.x is None and self.y is None:  
            return

        if self.y**2 != self.x**3 + a * x + b:  
            raise ValueError('({}, {}) is not on the curve'.format(x, y))

    def __eq__(self, other):  
        return self.x == other.x and self.y == other.y \
            and self.a == other.a and self.b == other.b

    # Exercise 2.2
    def __ne__(self,other):
        return not self.__eq__(other)

    def __add__(self, other):  
        if self.a != other.a or self.b != other.b:
            raise TypeError('Points {}, {} are not on the same curve'.format
            (self, other))

        # Exercise 2.7
        if self == other:
            s = (3 * self.x ** 2 + self.a) / (2 * self.y)
            x3 = s**2 - 2 * self.x 
            y3 = s * (self.x - x3) - self.y
            return self.__class__(x3,y3,self.a,self.b)

        if self == other and self.y == 0 * self.x:  
            return self.__class__(None, None, self.a, self.b)

        # Exercise 2.3
        if self.x == other.x and self.y != other.y:
            return self.__class__(None,None,self.a,self.b)

        if self.x is None:  
            return other

        if other.x is None:  
            return self

        # Exercise 2.5
        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x3 = s**2 - self.x - other.x 
            y3 = s * (self.x - x3) - self.y
            return self.__class__(x3,y3,self.a,self.b)

teste1 = FieldElement(3,13)
teste2 = FieldElement(5,13)
print(teste1 != teste2)
print(teste1 * teste2)