#Take 10 integer inputs from user and store them in a list and print them on screen.
"""
l=[]
for i in range(10):
    s=int(input())
    l.append(s)
print(l)
"""    
#Take 10 integer inputs from user and store them in a list.
#Again ask user to give a number.
#Now, tell user whether that number is present in list or not.
#( Iterate over list using while loop ).
""" 
i=4
l=[]
while i>0:
    s=int(input())
    l.append(s)
    i=i-1
print(len(l))
num=int(input("number "))
count=0
n=len(l)-1
while n>0:
    if num == l[n]:
        break
    elif num !=l[n]:
        count=count+1
    n=n-1
if num in l:
    print("found at ",count)
else:
    print("Not found")
"""    

"""
Take 20 integer inputs from user and print the following:
number of positive numbers
number of negative numbers
number of odd numbers
number of even numbers
number of 0s.

n=[]
pos=0
neg=0
odd=0
even=0
zero=0
for i in range(10):
    num=int(input())
    n.append(num)
for i in range(10):
    
    if n[i]>0:
        pos=pos+1
        if n[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    elif n[i]<0:
        neg=neg+1
        if n[i]%2==0:
            even=even+1
        else:
            odd=odd+1
    else:
        zero=zero+1
print("even",even)
print("odd",odd)
print("pos",pos)
print("neg",neg)
print("zero",zero)
"""

'''
Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.

l=[]
for i in range(10):
    num=int(input())
    l.append(num)
print("l",l)
l=l[::-1]
a=l
print(a)
print(a[::-1])
'''

'''
Write a program to find the sum of all elements of a list.

l=[1,2,3,4]
sum=0
for i in l:
    sum=sum+i
print(sum)
'''
'''
Write a program to find the product of all elements of a list.
l=[1,2,3,4]
pro=1
for i in l:
    pro=pro*i
print(pro)
'''
'''
Initialize and print each element in new line of a list inside list.

l=[[1,2],[2,3],[4,5]]
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
'''
'''
Find largest and smallest elements of a list.

l=[10,24,6,4,11]
max=l[0]
min=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
    elif l[i]<min:
        min=l[i]
print(max)   
print(min)
'''  
'''
Write a program to check if elements of a list are same or
not it read from front or back. E.g.-2	3	15	15	3	2

l=[2,3,15,15,3,2,4]
mid=(len(l))//2
found=True
for i in range(mid):
    if l[i]!=l[len(l)-i-1]:
        print("no")
        found=False
        break
if found==True:
    print("yes")
'''
'''
Make a list by taking 10 input from user. Now delete all repeated elements of the list.
E.g.-
INPUT : [1,2,3,2,1,3,12,12,32]
OUTPUT : [1,2,3,12,32]

l=[1,2,3,2,1,3,12,12,32]
print(list(set(l)))

####or

l=[1,2,3,2,1,3,12,12,32]
for i in range(len(l)):
    for j in range(i+1,len(l)-1):
        if l[i]==l[j]:
            del(l[j])
print(l)
'''

"""
Take a list of 10 elements. Split it into middle and store the elements
in two dfferent lists. E.g.-
INITIAL list :
58	24	13	15	63	9	8	81	1	78

After spliting :
58	24	13	15	63
9	8	81	1	78

l=[58,24,13,15,63,9,8,81,1,78]
mid=len(l)//2
c=l[:mid]
d=l[mid::]
print(c)
print(d)
"""
'''
Ask user to give integer inputs to make a list.
Store only even values given and print the list.
l=[]
n=int(input("how many numbers "))
for i in range(n):
    num=int(input())
    if num%2==0:
        l.append(num)
print(l)
'''
'''
Take a list of length n where all the numbers are non-negative and unique.
Find the element in the list possessing the highest value.
Split the element into two parts where first part contains the
next highest value in the list and second part hold the required
additive entity to get the highest value.
Print the list where the highest value get splitted into those two parts.
Sample input: 4 8 6 3 2
Sample output: 4 6 2 6 3 2


l=[4,8,6,3,2]
max=l[0]
for i in range(len(l)):
    if l[i]>max:
        max=l[i]
        index=i
del(l[index])
max2=l[0]
for j in range(len(l)):
    if max!=l[j] and l[j]>max2:
        max2=l[j]
        nex=max-l[j]
l.insert(index,max2)
l.insert(index+1,nex)

#print(l[:index]+[max2,nex]+l[index+1:])        
print(l)
'''
'''
Write a program to shift every element of a list to circularly right.
E.g.-
INPUT : 1 2 3 4 5
OUTPUT : 5 1 2 3 4

a = [1,2,3,4,5]
print (a)
b = [a[len(a)-1]]+a[:len(a)-1]
print (b)
'''
'''
Write a program to add and multiply two 3x3 matrices.
'''
from numpy import *

l1=matrix('1 2 3;1 2 3;1 2 3')
l2=matrix('4 5 6;4 5 6;1 2 3')
add=l1+l2
mul=l1*l2
print("add\n",add)
print("mul\n",mul)


