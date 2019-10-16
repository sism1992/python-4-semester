#lists in python

#husk: join, split, while, dictionary, set

l = ['A','n','d',3,'r',5]

a = l
print(type(l))
print(a)
print(id(a))
print(l)
print(id(l))

e = l[:]
print(e)
print(id(e))

print(l==e)
print(l is e)
print(l is a)

#loops

#foreach
for i in l:
    print(i)

for i in range(2, 10, 2):
    print(i)

#while

#append & pop
l.append('!')
print(l)
print(l.pop())
print(l)

#sorting
d = [10,8,9,18]
d.sort() #ændre listen
print(d)

#vender listen igen
d.reverse()
print(d)
print(sorted(d))

#sorted efter length # laver en ny liste
sd = ['Anders' , 'Thomas', 'Jonz']
print(sorted(sd, key=len))
print(sorted(sd, reverse=True))

#sorter efter  sidste bogstav
def sort_sidste_bogstav(t):
    return t[-1]

print(sorted(sd, key=sort_sidste_bogstav))

#sorter efter 4. bogstav
def sort_4_bogstav(t):
    return t[3]

print(sorted(sd, key=sort_4_bogstav))




#join

#split
# splitter string til elementer i list

#dictionary
#Samme som java map, kan feks indholde keys med lists
d = {'anders' : ['sej' , 'geniale'], 'thomas' : ['noob', 'ungster']}
d ['H'] = 'hello'
d ['H'] = 'world'
print(d.items())
print(d['anders'])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)
for k, v in d.items():
    print(k, '--->', v)

def f (x):
    return x[-1]

print(sorted(d.items(), key=f))

#set 
ss = {1,2,3,4,4,4}
sa = {1,2,54}
sds = set()
print(ss)
sa.union(ss)
print(sa)


#tuple - immutable
t = (1, 23, 5)
print(t)
print(type(t))
print(len(t))
print(t[1])
print(reversed(t))



