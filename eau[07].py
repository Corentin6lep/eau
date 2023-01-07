
def Minmaj(u):
    v=[]
    j=0
    for i in u:   #création d'un tableau 
        j=j+1
        v.append(i)

    for k in range(0,len(v)):      #identification de " " 
        if v[k]==" ":
            v[k+1]=v[k+1].upper()

    v[0]=v[0].upper()
    str=" ".join(v)
    print(str)

Minmaj("di or ra")