import random

class JellyBean:
    
    def __repr__(self):
        
        return str(self.__dict__)
    
    def __init__(self, name, ghost):
        
        self.__name = name
        self.__mass = (random.randint(1, 10))
        self.__formerMass = self.__mass
        #former liste
        self.stolenMassFrom = []
        #ghost  
        self.__ghost = ghost
        
        
    def __add__(self, other):
        
        #tester om man er har mistet mass til den pågældende, og om man er ghost, og at den man støder ind i ikke er ghost
        if(self.name in other.stolenMassFrom and self.ghost == True and other.ghost == False):
            self.ghost = False
            self.mass = self.formerMass
            other.mass -= self.formerMass
            self.formerMass = self.mass
            self.stolenMassFrom.append(other.name)
            if (other.__mass <= 0):
                other.ghost = True
                
        #HVIS BEGGE  ske noget
        elif (self.ghost == True and other.ghost == True):
            print('you are both ghost nothing happends')
            
            
        else:
            #hvis man ikke er stødt ind i hinanden før, og ens mass er over 0/ghost
            self.__mass += other.__mass
            other.__mass = 0
            other.ghost = True
            self.__formerMass = self.__mass
            # stjæle mass del
            self.stolenMassFrom.append(other.name)
            
                
        #altid med        
        print('{} mass is now {} and {} is now {}'.format(self.name, self.__mass, other.name, other.__mass))
    
    #former metode
    
    @property
    def ghost(self):
        return self.__ghost
    
    @property
    def name(self):
        return self.__name
    
    @property
    def mass(self):
        return self.__mass
    
    @property
    def formerMass(self):
        return self.__formerMass
    
    @ghost.setter
    def ghost(self, ghost):
        self.__ghost = ghost
    
    @mass.setter
    def mass(self, mass):
        self.__mass = mass
    
    @formerMass.setter
    def formerMass(self, x):
        self.__formerMass = x
    
    
    ## nedarv til fragement
    
jelly1 = JellyBean('Jelly 1', False)
jelly2 = JellyBean('Jelly 2', False)

print(jelly1)
print(jelly2)

jelly1 + jelly2

print(jelly1)
print(jelly2)

jelly2 + jelly1

print(jelly1)
print(jelly2)