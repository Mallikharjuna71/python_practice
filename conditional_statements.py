s = 'i am arjun 74'
r = ''
for i in s:
    if i.isalpha():
        i = i.upper()
        r += i
    elif i.isdigit():
        i = int(i)
        if i %2 == 0:
            i = i*2
            i = str(i)
        else:
            i += 1
            i = str(i)
        r += i
    else:
        r += i

print(r)

number = int(input('enter a number: '))
if number < 0:
    print('it is a negative number')
elif (number > 0) and (number <= 100):
    print('it is a positive number less than or equal to 100')
else:
    print('number is greater than 100')

