nbrpremier=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def u(a):
    i=0
    if a< 0 :
        print('-1')
        exit
               
    else:
        while nbrpremier[i] < a :
            i=i+1
        print(nbrpremier[i]) 
    
    
u(12)