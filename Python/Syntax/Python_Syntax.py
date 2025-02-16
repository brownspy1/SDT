def add(a,b):
    return a+b
def print_num(num):
    for i in range(1,num+1):
        print(i);

a = int(input())
b = int(input())

print(add(a,b))
print_num(a)

if(a < 5):
    print("hello")
elif(a>10):
    print("Hello world")
else:
    print("abraka dabra")
