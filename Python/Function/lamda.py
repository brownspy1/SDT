def brr(fun,val):
    return 5+fun(val)

sqrt = lambda x: x**2
print(sqrt(5))
print(brr(lambda a: a*a*2,5))
