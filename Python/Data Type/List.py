#---------------------------------list--------------------------------------
# lis = []
# lis.extend([1,2,3,4,5,6])
# lis.insert(6,7)
# lis.append(8)
# lis.remove(8)
# lis.pop(6)
# print(lis)
# lis.sort(reverse=True)
# print(lis)
# lis.reverse()
# print(lis)
# ls = []
# ls = lis[0:4]
# print(ls)
# print(len(lis))
# for i in lis:
#     print(i,end=" ")
#
# ls = [1, 2, 3, 4, 5, 3]
# # numbers = [i for i in numbers if i!= 3] # list Comprehensions
# ls.pop()
# print(ls)

# -----------------------------------list Comprehensions -------------------------------------------------------
# ls = []
# n = int(input())
# ls = [num for num in range(2,n+1) if num%2==1 if num%5==0]
# print(ls)
ls = [0,1,0,1,1,0]
fs = [0,1,0,1,1,0]
ps = [0,1,0,1,1,0]
ps.reverse()
fs.sort(reverse=True)
ans = [[i,j,k] for i in ls for j in fs for k in ps]
print(ans)
