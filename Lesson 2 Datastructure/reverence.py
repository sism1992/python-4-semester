# reverence a text string

#vender en string via 'slicing'
def reverse(text):
    return text[::-1]

#vender en string via list
def revers_with_methods(text):
    
    #'' - er hvad der skal være mellem hver værdi i listen
    text = ' '.join(reversed(text))
    return text

#mine variabler
s = revers_with_methods('rettus samohT')
b = reverse('jes re srednA go')

print (s)
print (b)