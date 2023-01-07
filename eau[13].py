def selec(n):
    
    for i in range(0,len(n)):
        for j in range(0,len(n)):
            if n[j]>n[i]:
                a=n[i]
                n[i]=n[j]
                n[j]=a
    print(n)

selec([6,5,4,3,2,1])