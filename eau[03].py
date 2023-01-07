
def Fibo(n):
    a=0
    b=1
    d=0
    for i in range(0,n-1):
        d=a+b
        a=b
        b=d
    print(d)
Fibo(2)