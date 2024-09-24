# name = input('enter your name: ')
# age = input('enter your age: ')
#
# def greeting(i, n):
#     print(f"Hi {i} you are {n} years old")
#
# greeting(name, age)
#
# def sum(*n):
#     total = 0
#     for i in n:
#         total += i
#     print(total)
#
# sum(2, 5, 6, 8, 10, 45)
#
# def merge_the_tools(string, k):
#     # your code goes here
#     pp = len(string)//k
#     wl = []
#     nwl = []
#     for i in range(pp):
#         w = string[:k]
#         wl.append(w)
#         string = string[k:]
#     for word in wl:
#         word = list(word)
#         el = []
#         for i in word:
#             if i not in el:
#                 el.append(i)
#         nw = ''.join(el)
#         nwl.append(nw)
#     for i in nwl:
#         print(i)
#
#
# merge_the_tools('asdfghjkl', 3)
#
#
# def greet(name):
#     return f"Hi {name} have a good day"
#
#
# def hof(func):
#     r = func('reddy')
#     r.upper()
#     print(r)
#
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# def even(i):
#     return i*10+8
#
# r = map(even, l)
# print(*r)
#
# from functools import reduce
#
# l = [1, 2, 3, 4, 5, 6, 7, 8]
# r = reduce(lambda x, y: x+y, l, 10)
# print(r)
#
#

# import numpy
#
# array = [[2, 5], [3, 7], [1, 3], [4, 0]]
# def max_of_min(array):
#     array = numpy.array(array)
#     mn = numpy.min(array, axis=1)
#     print(numpy.max(mn))
#
#
# array = [ [1, 2], [3, 4] ]
#
# # mean, var, std = 1 , 0, None
# def mean_varianc_std(n):
#     array = numpy.array(n)
#     print(numpy.mean(array, axis=1))
#     print(numpy.var(array, axis=0))
#     print(numpy.std(array, axis=None))
# mean_varianc_std(array)
#153, 31, 57
array = [1, 5, 3]
a = {3, 1}
b = {5, 7}
def no_idea(array, a, b):
    total = 0
    for i in array:
        if i in a:
            total += 1
        if i in b:
            total -= 1
    return total

print(no_idea(array, a, b))

def filing_up(a):
    pass