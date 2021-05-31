def tower(n,beg,end,aux):
    if n == 1:
        print("Move disk 1 from rod",beg,"to rod",end)
        return
    tower(n-1,beg,aux,end)
    print("Move disk",n,"from rod",beg,"to rod",end)
    tower(n-1,aux,end,beg)
n=3
tower(n,'A','C','B')
 
  
