'''
1) 2) Write a function to calculate area and perimeter of a rectangle

def area(l,b):
    return l*b
def peri(l,b):
    return 2*(l+b)
print(area(10,20))
print(peri(10,20))
'''
'''
3) Write a function to calculate power of a number raised to other. E.g.- a^b.

def power(a,b):
    return a**b
print(power(2,10))
'''
'''
4) Write a function to tell user if he/she is able to vote or not.
( Consider minimum age of voting to be 18. )

def vote(age):
    if age<18:
        print('invalid')
    else:
        print('valid')
vote(10)
'''
'''
5) Print multiplication table of 12 using recursion.

def mul(n,i):
    print("{} * {} = {} ".format(n,i,n*i))
    i+=1
    if i<=10:
        mul(n,i)
mul(12,1)
'''
'''
6) Write a function to calculate power of a number raised
to other ( a^b ) using recursion.

def power(a,b):
    if b==1:
        return a
    else:
        return a*power(a,b-1)
print(power(2,4))
'''
'''
7) Write a function “perfect()” that determines if parameter number is a
perfect number. Use this function in a program that determines and prints all
the perfect numbers between 1 and 1000.
[An integer number is said to be “perfect number” if its factors, including
1(but not the number itself), sum to the number. E.g., 6 is a perfect number
because 6=1+2+3]

def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
    if sum==n:
        return True
    else:
        return False
for i in range(1,1001):
    if perfect(i):
        print(i)
'''
'''
8) Write a function to check if a number is even or not.

def even(n):
    if n%2==0:
        print('even')
    else:
        print('odd')
even(15)
'''
'''
9) Write a function to check if a number is prime or not.

def prime(n):
    found=True
    for i in range(2,n):
        if (i**2)<n:
            if n%i==0:
                print('not')
                found=False
        break   
    if found:
        print('prime')
prime(222222222227)
'''
'''
10)Write a function to find factorial of a number but also store the factorials calculated in a dictionary

d={0:1,1:1}
def fact(n):
    if n in d.keys():
        return d[n]
    else:
        fa= n*fact(n-1)
        d[n]=fa
        return fa
print(fact(5))
print(d)
'''

