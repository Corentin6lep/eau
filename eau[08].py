def u(n):
    j=0
    A=(1,2,3,4,5,6,7,8,9)
    B=('1','2','3','4','5','6','7','8','9')
    n=str(n)
    for i in n:
        if i in A or i in B :
            j=j+1
    if j==len(n):
        print("True")
    else:
        print('False')    
u(532415)