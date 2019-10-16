class S:
    
    def __init__(self):
        self.name = 'Claus'
        self.sir = 'Bove'

    #represenetere objektet formelt
    def __repr__(self):
        return str(self.__dict__)
    
    #mere tostring agtig
    def __str__(self):
        return self.name
    
    def __add__(self, other):
        return self.name + other.name
        return self.sir + other.sir
    
    def __call__(self):
        return 'bla bla'
    
s = S()
s2 = S()
s2.name = ' tosse'
s2.sir = ' tosse'

print(s)
print(repr(s))
print(str(s))

s3 = s+s2

print(repr(s3))
print(s())