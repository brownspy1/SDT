#---------------------------------list--------------------------------------
lis = []
lis.extend([1,2,3,4,5,6])
lis.insert(6,7)
lis.append(8)
lis.remove(8)
lis.pop(6)
print(lis)
lis.sort(reverse=True)
print(lis)
lis.reverse()
print(lis)
ls = []
ls = lis[0:4]
print(ls)
print(len(lis))
for i in lis:
    print(i,end=" ")      
    