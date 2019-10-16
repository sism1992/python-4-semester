class Car:
    
    def __init__(self, make, model, bhp, mph):
        self.__make = make
        self.__model = model
        self.__bhp = bhp
        self.__mph = mph
    
    def tell(self):
        print("This car is a {} {} with {} and a top speed of {} mph".format(self.__make, self.__model, self.__bhp, self.__mph))
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, make):
        self.__make = make
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
        
    @property
    def bhp(self):
        return self.__bhp
    
    @bhp.setter
    def bhp(self, bhp):
        self.__name = bhp
    
    @property
    def mph(self):
        return self.__mph
    
    @mph.setter
    def mph(self, mph):
        self.__mph = mph
        
accNum_list = []

class Bank:    
    def __init__(self):
        self.__accounts = []
        
    @property
    def accounts(self):
        return self.__accounts
    
    
    
    def addAccount(self, account):
        if account not in self.__accounts and account.no not in accNum_list and account.cust.age >= 18:
            self.__accounts.append(account)
            accNum_list.append(account.no) 
        
        else:
            print('you can only have 1 account')
        

class Account:
    def __init__(self, no, cust):
        self.__no = no
        self.__cust = cust
        
       
        
    @property
    def no(self):
        return self.__no
    
    @no.setter
    def no(self, no):
        self.__no = no
    
    @property
    def cust(self):
        return self.__cust
    
    @cust.setter
    def cust(self, cust):
        self.__cust = cust

class Customer:
    def __init__(self, name, age):
        self.__age = age
        self.__name = name
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age <= 17:
            self.__age = age
        else:
            print('you have to be over 18 to be a customer')
            
# lav cust
thomas = Customer('Thomas', 17)         #burde ikke virke
anders = Customer('Anders', 28)         #burde virke

# lav acc
accThomas = Account(1, thomas)
accAnders = Account(1337, anders)
accThomas2 = Account(2, thomas)

# lav bank
winBank = Bank()

#tilføje accounts
print('thomas 1')
winBank.addAccount(accThomas)
print('anders 1')
winBank.addAccount(accAnders)
print('thomas 2')
winBank.addAccount(accThomas2) # burde ikke virke
print('anders 2')
winBank.addAccount(accThomas) #burde ikke virke

print(winBank.accounts)
for i in winBank.accounts:
    print(i.cust.name)

