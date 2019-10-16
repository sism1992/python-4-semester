import sys 
from classTest import Sushi

nigiri = Sushi('shake', 'nigiri',25)

maki = Sushi('california', 'maki', 100)


maki.make()
nigiri.make()
print(nigiri.name)

maki.name = 'thomas'
print(maki.name)

maki.name2 = 'thomas'
print(maki.name)