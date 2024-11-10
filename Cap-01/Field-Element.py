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

    # Exercise 1
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __add__(self, other):
        if self.prime != other.prime:  
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime  
        return self.__class__(num, self.prime)
    
    # Exercise 3
    def __sub__(self,other):
        if self.prime != other.prime:  
            raise TypeError('Cannot subtract two numbers in different Fields')
        num = (self.num - other.num) % self.prime  
        return self.__class__(num, self.prime)
    
    # Exercise 6
    def __mul__(self,other):
        if self.prime != other.prime:  
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime  
        return self.__class__(num, self.prime)

teste1 = FieldElement(3,13)
teste2 = FieldElement(5,13)
print(teste1 != teste2)
print(teste1 * teste2)