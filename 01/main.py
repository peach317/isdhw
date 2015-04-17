for i in range(1,10):
        print(" "*7*i,end="")
        for j in range(i,10):
            s=str.format("{0:1}*{1:1}={2:<3}",i,j,i*j)
            print(s,end="")
        print()
