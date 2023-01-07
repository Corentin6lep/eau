u=[20,5,1,19,21]
v=[]
for i in u:
    for j in u:
        a=abs(j-i)
        if a != 0:
            v.append(a)
print(min(v))