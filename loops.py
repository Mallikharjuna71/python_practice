import random
guess = random.randint(0, 10)
number = int(input('enter a number 0 to 10: '))

while number != guess:
    print('you got it wrong ')
    number = int(input('enter a number 0 to 10:   '))
print('your guess is correct')


l = [1, 2, 'a', [20, 30, 40, 6, 7], ['b', 'c']]
nl = []
wl = []
for i in l:
    if type(i)==int:
        nl.append(i)
    elif type(i)==str:
        wl.append(i)
    elif type(i)==list:
        for j in i:
            if type(j)==int:
                nl.append(j)
            if type(j)==str:
                wl.append(j)

print((*wl, *nl))


