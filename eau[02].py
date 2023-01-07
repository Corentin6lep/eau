def verlan(*argv):
    B=[*argv]
    C=""
    D=" "
    n=len(B)
    for i in range(0,n):
        if isinstance(B[i],str):
            c=n-i-1                        #i ne peut pas valoir n et on commence à compter à partir de 0 (ex: si i=0 alors B[3]=>"?")
            C=C+B[c]
            C=C+D
        else:
            
            exit
    print(C)

verlan("alors","c'est","bon","?",)