#to find all roots of a quadratic equation ax2+bx+c=0.
import math as m
def f(a,b,c):
    D=(b**2)-(4*a*c)
    if D>0:
        s=m.sqrt(D)
        r1=(-b+s)/(2*a)
        r2=(-b-s)/(2*a)
        print ("{} and {}".format(r1,r2),end="")
        print("are roots")
    else:
        t=-(D)
        u=m.sqrt(t)
        real=b/(2*a)
        img=u/(2*a)
        print("{}+j{}".format(real,img),end="")
        print("{}-j{} are roots".format(real,img))

f(1,5,6)      
            
