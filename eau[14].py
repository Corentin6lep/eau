A=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
B=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


u=["Alfred","Momo","Gilbert"]

C=len(u)*[1]
for i in range(0,len(u)):
    d=0
    for j in B:
        d=d+1
        if u[i][0]==j:
            C[i]=d

for i in range(0,len(u)):
    for j in range(0,len(u)):
        if C[i]>C[j]:
            a=u[i]
            u[i]=u[j]
            u[j]=a
print(u)