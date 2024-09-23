name = input('enter your name: ')
age = input('enter your age: ')

def greeting(i, n):
    print(f"Hi {i} you are {n} years old")

greeting(name, age)

def sum(*n):
    total = 0
    for i in n:
        total += i
    print(total)

sum(2, 5, 6, 8, 10, 45)

def merge_the_tools(string, k):
    # your code goes here
    pp = len(string)//k
    wl = []
    nwl = []
    for i in range(pp):
        w = string[:k]
        wl.append(w)
        string = string[k:]
    for word in wl:
        word = list(word)
        el = []
        for i in word:
            if i not in el:
                el.append(i)
        nw = ''.join(el)
        nwl.append(nw)
    for i in nwl:
        print(i)


merge_the_tools('asdfghjkl', 3)


def greet(name):
    return f"Hi {name} have a good day"


def hof(func):
    r = func('reddy')
    r.upper()
    print(r)

l = [1, 2, 3, 4, 5, 6, 7, 8]
def even(i):
    return i*10+8

r = map(even, l)
print(*r)

from functools import reduce

l = [1, 2, 3, 4, 5, 6, 7, 8]
r = reduce(lambda x, y: x+y, l, 10)
print(r)




