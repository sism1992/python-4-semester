#https://docs.python.org/3/library/functions.html#open
#git commit -a -m"bla bla"
f = open ('test.txt', 'w') #overwrite
f.write('Hello there i am writing to this file')
f.close()

#with
with open('test.txt', 'r') as f:

#1 
# for i in f:
    print(i.read()) ##en linje af gangen i ram
    print(i)

#2
print(f.readlines())

#3
print(f.read())

#4 
print(f.readline())



#try/catch
try:
    f.open('fejlMedVilje.txt', 'r')
    print(f.read())
except:
    print('booo')