def u(*argv):
    B=[*argv]
    n=len(B)
    g=''
    for i in range(0,n):
        for j in B[i]:
            if j in B[1]:
                g="True"
            else:
                g="False"

    return print(g)

u("Bonjour", "jour")

