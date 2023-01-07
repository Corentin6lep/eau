A=[]
for i in range (0,101):
    B=[i]
    A=A+B       #concatener deux listes

for j in A:
    for k in A:
        if j<A[k]:
            print(j,"<",A[k])