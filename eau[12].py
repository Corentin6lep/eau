def tri(u):
    j=0
    while u[0]>u[1]:
        for i in range(0,len(u)-1):
                if u[i]>u[i+1]:
                    c=u[i+1]
                    u[i+1]=u[i]
                    u[i]=c
    print(u)

tri([5,4,3,2,1])
