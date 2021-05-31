"""GCD of 2 numbers"""

n1=int(input("number 1: "))
n2=int(input("number 2: "))
i=1
while(i<=n1 and i<=n2):
    if(n1%i==0 and n2%i==0):
        gcd=i
    i=i+1
print("GCD of {} and {} is".format(n1,n2),gcd)


"""prime number
u=10
l=2
print("Prime")
for i in range(l,u+1):
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            print(i)

            
"""

"""#leap
year=int(input("Year: "))
if((year%4)==0 and year%100!=0) or ((year%400)==0):
    print("Leap year")
else:
    print("Not leap")"""

"""
strong number - 1!+4!+5!=145

n=int(input("number"))
temp=n
Sum=0
while(temp>0):
    fact=1
    i=1
    d=temp%10
    while(i <= d):
        fact=fact*i
        i=i+1
    Sum=Sum+fact
    temp=temp//10
    
if(Sum==n):
    print("Strong number")
else:
    print("not strong number")

"""


"""
Factorial


n=int(input("number: "))
fact=1
temp=n
if(n>0):
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
else:
    print("Invalid num")"""
"""
palindrome number

n=int(input("number"))
temp=n
reverse=0
while(temp>0):
    d=temp%10
    reverse=(reverse*10)+d
    temp=temp//10
if(n==reverse):
    print("Palindrome");
else:
    print("Not palindrome");
    """
"""
palindrome string

n=input("String: ")  
rev = n[::-1]
if (n == rev):
    print("Palindrome")
else:
    print("Not palindrome")

"""
  
  


#pattern a)
"""
formula:

n   i    star   space
5   0     1      8
5   1     3      6
5   2     5      4
5   3     7      2
5   4     9      0

        *
       ***
      *****
     *******
    *********

n=5
space=2*n-2
star=1

for i in range(0,n):
    for j in range(0,space):
        print(end=" ")
    space=space-1
    for k in range(0,star):
        print("*",end="")
    star=star+2
    print()
    """

"""
# pattern b
A 

B B 

C C C 

D D D D 

E E E E E
n=5
c=['A','B','C','D','E']
for i in range(0,n):
    print()
    for j in range(0,i+1):
      
        print(c[i],end=" ")
    print()
    """

"""
#pattern c
* * * * *
* * * *
* * * 
* *
*
n   i   star
5   0    5
5   1    4
5   2    3


n=5
for i in range(0,n):
    star=n-i
    for j in range(0,star):
        print("*",end=" ")
    print()
    """
"""
pattern d)
1 2 3 4 5
1 2 3 4 
1 2 3
1 2
1

n=5
for i in range(0,n):
    num=n-i
    for j in range(1,num+1):
        print(j,end=" ")
    print()

"""
