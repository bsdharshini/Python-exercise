'''
1) Print all elements of a list using for loop.
l=[1,2,3,4]
for i in l:
    print(i)
'''
'''
2) Take inputs from user to make a list.
Again take one input from user and search it in the list and
delete that element, if found.Iterate over list using for loop.

l=[]
for i in range(5):
    num=input()
    l.append(num)
s=input('jjj')
if s in l:
    del(l[l.index(s)])
print(l)
'''  
'''
3) Print multiplication table of 14 from a list in which
multiplication table of 12 is stored.

l=[12,24,36,48,60,72,84,96,108,120]
l1=[]
l2=[2,4,6,8,10,12,14,16,18,20]
i=0
for a in l:
    a=a+i+2
    i+=2
    l1.append(a)
j=1
for i in l1:
    print("14 * {} = {}".format(j,i))
    j+=1
'''
'''
4) You are given with a list of integer elements.
Make a new list which will store square of elements of previous list.

l=[1,2,3,4]
l1=[]
for i in l:
    i=i**2
    l1.append(i)
print(l1)
'''
'''
5) Using range(1,101), make two list,
one containing all even numbers and other containing all odd numbers.

6) From the two list obtained in previous question, make new lists,
containing only numbers which are divisible by 4, 6, 8, 10, 3, 5, 7 and 9 in
separate lists.

l1,l2,four,six,eight,ten,three,five,seven,nine=[],[],[],[],[],[],[],[],[],[]
for i in range(1,101):
    if i%2==0:
        l1.append(i)
    elif i%2!=0:
        l2.append(i)
for j in l1:
    if j%4==0:
        four.append(j)
    if j%6==0:
        six.append(j)
    if j%8==0:
        eight.append(j)
    if j%10==0:
        ten.append(j)
    if j%3==0:
        three.append(j)
    if j%5==0:
        five.append(j)
    if j%7==0:
        seven.append(j)
    if j%9==0:
        nine.append(j)
for j in l2:
    if j%4==0:
        four.append(j)
    if j%6==0:
        six.append(j)
    if j%8==0:
        eight.append(j)
    if j%10==0:
        ten.append(j)
    if j%3==0:
        three.append(j)
    if j%5==0:
        five.append(j)
    if j%7==0:
        seven.append(j)
    if j%9==0:
        nine.append(j)
three.sort()
four.sort()
five.sort()
six.sort()
seven.sort()
eight.sort()
nine.sort()
ten.sort()
print("even ",l1,"\n")
print('odd ',l2,"\n")
print('three ',three,"\n")
print('four ',four,"\n")
print('five ',five,"\n")
print('six ',six,"\n")
print('seven ',seven,"\n")
print('eight ',eight,"\n")
print('nine',nine,"\n")
print('ten ',ten,"\n")
'''
'''
7) From a list containing ints,
strings and floats, make three lists to store them separately

l=[1,'aaa',1.245]
integer=[]
fl=[]
string=[]
for i in l:
    if type(i)==int:
        integer.append(i)
    elif type(i)==str:
        string.append(i)
    elif type(i)==float:
        fl.append(i)
print(integer)
print(fl)
print(string)
'''
'''
8) Using range(1,101), make a list containing only prime numbers.

l=[]
for i in range(2,101):
    isPrime=True
    for j in range(2,i):
        if i%j==0:
            isPrime=False
    if isPrime:
        l.append(i)
print(l)      
'''
'''
9) Initialize a 2D list of 3*3 matrix. E.g.-
1	2	3
4	5	6
7	8	9

Check if the matrix is symmetric or not.

m=[[1,1,1],[1,1,1],[1,1,1]]
sym=True
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j]!=m[j][i]:
            sym=False
print(sym)
'''

'''
10) Sorting refers to arranging data in a particular format.
Sort a list of integers in ascending order ( without using built-in sorted function ).
One of the algorithm is selection sort. Use below explanation of selection sort to do this.
INITIAL LIST :
2	3	1	45	15
First iteration : Compare every element after first element with first element and if it is larger then swap.
In first iteration, 2 is larger than 1. So, swap it.
1	3	2	45	15
Second iteration : Compare every element after second element with second element and if it is larger then swap.
In second iteration, 3 is larger than 2. So, swap it.
1	2	3	45	15
Third iteration : Nothing will swap as 3 is smaller than every element after it.
1	2	3	45	15
Fourth iteration : Compare every element after fourth element with fourth element and if it is larger then swap.
In fourth iteration, 45 is larger than 15. So, swap it.
1	2	3	15	45

l=[2,3,1,45,15]
for i in range(len(l)):
    for j in range(i):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
print(l)
'''
