create = input('New user or exsisting user?\n N for new\n E for exsisting: ')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

if create == 'N':
    username = input('enter username: ')
    passw = input('enter password: ')
    print('all done')
    f = open('users.txt', 'a+')
    f.write(username + ' ' + passw + '\n')
    f.close()
    
elif create =='E':
    f = open('users.txt', 'r')
    users = f.read()
    f.close()
    users_dict = {}

    detailsList = users.split()

    givenName = input('Type username: ') 
    givenPass = input('Type password: ')

    for i in range(0,file_len('users.txt')+1,2):
        users_dict[detailsList[i]] = detailsList[i+1]
    try:
        if users_dict[givenName] == givenPass:
            print('your in')
    except:
        print('lol wrong password or username')
    

else:
    print('wrong input, only N or E')