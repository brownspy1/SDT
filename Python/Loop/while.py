# --------------primality test--------------
# i = 2
# n = int(input())
# lis = []
# while i < n+1:
#     flag = True
#     j = 2   
#     while j < i:
#         if i%j==0:
#             flag = False
#             break
#         j+=1
#     if flag:
#         lis.append(i)
#     i+=1
# print(len(lis))

#--------------------even odd ---------------
i = 1
n = int(input())
 
while i < n+1:
    if i%2 == 0:
        i += 1
        continue
    print(i,end=" ")
    i+=1
i = 1
print("")
print("---------------------------------------------")
while i < n+1:
    if i%2 != 0:
        i+=1
        continue
    print(i,end=" ")
    i+=1
