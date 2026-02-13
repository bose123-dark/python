from functools import reduce


def num(a,b):
    return a + b ,num
result=[10,20,30]

var=(reduce(lambda a,b : a+b ,result))

print(var)
