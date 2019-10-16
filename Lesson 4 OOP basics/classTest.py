class Sushi:
    
    origin = 'asia'
     
    def __init__(self, name, type, price):
        self.__name = name
        self.__type = type
        #private __
        self.__price = price
        
    def make(self):
        print("{} is a {} that cost {}$".format(self.__name, self.__type, self.__price))
    
    #fancy python getter
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if not 'thomas' in name:
            self.__name = name
        else:
            print('moron')
        
        
    """
    #Getter oldschool   
    def get_name(self):
        return self.__name
    
    #Setter oldschool
    def set_name(self, newName):
        self.__name = newName
    """




