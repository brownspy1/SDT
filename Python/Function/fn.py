def add(*args):
    ans = 0
    for i in args:
        ans += i
    return ans
def sub(a,b,c):
    return a+b-c
def mul(*args):
    ans = 1
    for i in args:
        ans *= i
    return ans
def div(*args):
    ans = 1
    for i in args:
        ans/=i
    return ans