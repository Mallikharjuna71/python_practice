l = [1, 2, 3, 'arjun']

l.append(4)
print(l)
print(l.index('arjun'))
l.insert(0, 'i will be at index zero')
print(l)
l[0] = 0
print(l)
l = l[::-1]
marks = [10, 8, 9]
min = min(marks)
max = max(marks)
sum = sum(marks)
print(f"min:{min}, max:{max}, sum:{sum}")
k = l.pop()
print(l)
print(f"pop item {k}")

l.remove('arjun')
print(l)
l.sort()
print(l)
l = sorted(l, reverse=True)
print(l)
k = [6, 7, 8]
l.append(k)
print(l)
l.extend(k)
print(l)
l.remove([6, 7, 8])
print(l)



