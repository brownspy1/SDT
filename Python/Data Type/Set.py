st = {1,2,3,4,5,1,2,3,4} #contain uniq
st.add(5)
st.add(6)
print(st)
st.update([7,8,9])
print(st)
st.remove(5)
print(st)
st.discard(1)
st.discard(10)#don't get error
print(len(st))
print(st)
st.pop()
st.pop()
st.clear()
st.add(0)
print(st)


#------------------ Mathematical Operations-------------
a = {1,2,3}
b = {3,4,5}

print(a | b) # union
print(a & b) # intarsection
print(a - b) # defarencition
print(b - a) # defarencition
print(a ^ b) # Symmetric Difference 