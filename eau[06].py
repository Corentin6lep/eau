def Majmin(u):
    n=len(u)
    v=len(u)*[0]
    for i in range(0,n):
        s=str(u[i])
        if i%2 ==0:
            b=s.upper()
            v[i]=b
        else:
            b=s.lower()
            v[i]=b
    n="".join(v)
    print(n)


Majmin("Bonjour comment")