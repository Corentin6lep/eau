A=[0,1,2,3,4,5,6,7,8,9]

for i in A:
    for j in A:
        for t in A:
            if t>j and j>i:
                print (A[i],A[j],A[t])

