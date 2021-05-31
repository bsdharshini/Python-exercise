'''
Take 10 integers from keyboard using loop and print their
average value on the screen.

sum=0
for i in range(0,10):
    n=int(input())
    sum=sum+n
print(sum)
'''

'''
Print the following patterns using loop :
a.
*
**
***
****

n i star
4 0  1
4 1  2


n=int(input())
for i in range(0,n):
    print()
    for j in range(0,i+1):
        print("*",end="")
'''
'''
b.
  *  
 *** 
*****
 *** 
  *

n i  space star
5 0   4     1
5 1   2     3
5 2   0     5

5 3   2     3
5 4   4     1


n=int(input())
i,j,k=0,0,0
space=n-(2*i)-1
for i in range(0,n):
    for j in range(0,space):
        print("")
        space-=1
        for k in range(0,(n-space)):
            print("*",end="")
    for j in range(0,space+2):
        print("")
        for k in range(0,(n-space)):
            print("*",end="")     
        
print()

'''

'''
Print multiplication table of 24, 50 and 29 using loop.

for i in range(1,11):
    one=24*i
    print("24 * {} =".format(i),one)
print("\n")
for j in range(1,11):
    two=50*i
    print("50 * {} =".format(j),two)
print("\n")
for k in range(1,11):
    three=29*i
    print("29 * {} =".format(k),three)
print("\n")
'''


'''
Factorial of any number n is represented by n! and is equal to 1*2*3*....*(n-1)*n. E.g.-
4! = 1*2*3*4 = 24
3! = 3*2*1 = 6
2! = 2*1 = 2
Also,
1! = 1
0! = 1
Write a program to calculate factorial of a number.

n=int(input())
fact=1
for i in range(1,n+1):
    fact=fact*i
    n
    
print(fact)

'''
"""
Take integer inputs from user until he/she presses q
( Ask to press q to quit after every integer input ).
Print average and product of all numbers.
"""
n=0
su=0
product=1
while(n!='q'):
    n=int(input())
    su+=n
    product*=n
print(su)
print(product)
    


