import random

class JellyBean:
    
    def __repr__(self):
        
        return str(self.__dict__)
    
    def __init__(self, name, ghost):
        
        self.__name = name
        self.__mass = (random.randint(1, 10))
       
        #former liste
        self.stolenMassFrom = {}
        #ghost  
        self.__ghost = ghost
        
        
    def __add__(self, other):
        
        #tester om man er har mistet mass til den pågældende, og om man er ghost, og at den man støder ind i ikke er ghost
        if(self.name in other.stolenMassFrom.keys() and self.ghost == True and other.ghost == False):
            #checker dict for hvor meget self har mistet til 'other' og ligger det til sit eget mass
            self.mass += other.stolenMassFrom[self.name]
            #trækker den 'tilbage-erobret' mass fra 'other'
            other.mass -= other.stolenMassFrom[self.name]
            #fjerner selve key' i dict efter værdien er aflæst
            del other.stolenMassFrom[self.name] 
            
            
            #fjerner en fra 'ghost status' hvis man har mere end 0 i mass
            if(self.mass > 0):
                self.ghost = False
            
                       
                
        #HVIS BEGGE  ske noget
        elif (self.ghost == True and other.ghost == True):
            print('you are both ghost nothing happends')
            
        #hvis man ikke er stødt ind i hinanden før, og ens mass er over 0/ghost
        else:
            self.stolenMassFrom[other.name] = other.mass
            self.mass += other.mass
            other.mass = 0
            other.ghost = True
            
                
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
    
    @ghost.setter
    def ghost(self, ghost):
        self.__ghost = ghost
    
    @mass.setter
    def mass(self, mass):
        self.__mass = mass
    

    
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