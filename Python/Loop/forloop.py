# import math
# n = int(input())
# lis = []
# for i in range(2,n+1):
#     flag = True
#     for j in range(2,int(math.sqrt(i))+1):
#         if i%j==0:
#             flag = False;
#             break
#     if flag :
#         lis.append(i)
# print(len(lis))

#--------------------------------even 
n = int(input())
cnt = 0
for i in range(1,n+1):
    if(i%2==0):
        continue
    cnt+=1
    print(i,end=" ")
print("count: ",cnt,end=" ")