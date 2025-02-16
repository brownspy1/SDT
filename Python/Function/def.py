# def add(a,b,c=0):
#     return a+b+c
# print(add(10,20,30))
# print(add(10,20))
def add(*args): # add with args
    sum = 0;
    for i in args:
        sum+=i
    return sum;
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))
print(add(10,20,30,40,50))

