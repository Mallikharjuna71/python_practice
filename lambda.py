k = lambda x, y : x*y

print(k(3, 9))

def cp(s):
    r = lambda n: s +" "+ n
    return r


m = cp('hi')
print(m('hello'))




