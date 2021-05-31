'''
a = [1, 2, 3]
b = [1, 2, 3]
if a == b:
 print("list are equal")
else:
 print("list are not equal")
a.append(b)
print(a)
'''
'''
a = [1, 2, 3]
b = [1, 2, 3]
a.extend(b)
print(a)
a.insert(2,20)
print(a)
a.insert(4,[4, 5, 6])
print(a)
'''
'''
a = [1,2,3,4]
b = tuple(a)
print(b)
'''
'''

a1, a2, a3, a4 = 1, 2, 3, 4
print(a1)
print(a2)
print(a3)
print(a4)
b = 1,2,3,4,5
print(type(b))
print(b)

'''
'''
a = { "a" : 1, "b" : [1,2,3],  (1,2,3) : [1,2,3] }
print(a)
print(a.keys())
print(a.values())
print(a[(1,2,3)])
'''
'''
def myfunc(n):
 return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(4))
'''
'''
a = [x for x in range(10)]
b = list(map(str,a))
print(b)
'''



'''
String list to int list

l1=['1','2']
for i in range(0, len(l1)): 
   l1[i] = int(l1[i])
print(l1)
'''

'''
print the values from the dictionary

d1={'a':1,'b':2,'c':3}
print(d1.values())
'''
'''
to replace a alphabet by # in the given string

s='abababc'
s=s.replace('a','#')
print(s)
'''

'''
4.	Write a program to swap two numbers

x,y=10,5
x,y=y,x
print(x,y)
'''
'''
to remove the numbers in a given String

s=input()
s1=''.join([i
for i in s
    if not i.isdigit()])
print(s1)
'''
'''
to replace a consonant by * in the given String

s=input()
for i in s:
    if(i=='a')or (i=='e') or (i=='i') or (i=='o') or(i=='u'):
        pass
    else:
        s=s.replace(i,'*')
print(s)

'''
'''
to add two matrices


X = [[1,2,3], 
	[7 ,8,9]] 

Y = [[9,8,7],  
	[3,2,1]] 


result = [[0,0,0],  
		[0,0,0]] 
if len(X)==len(Y):
    for i in range(len(X)):
        for j in range(len(X[0])):
            result[i][j] = X[i][j] + Y[i][j] 

for r in result: 
	print(r) 

'''
'''
to multiply to matrices

A = [[12, 7, 3], 
	[4, 5, 6], 
	[7, 8, 9]] 	 
B = [[5, 8, 1, 2], 
	[6, 7, 3, 0], 
	[4, 5, 9, 1]] 
	
result = [[0, 0, 0, 0], 
		[0, 0, 0, 0], 
		[0, 0, 0, 0]] 
for i in range(len(A)): 
	for j in range(len(B[0])):  
		for k in range(len(B)): 
			result[i][j] += A[i][k] * B[k][j] 
for r in result: 
	print(r)
''' 
'''
to swap 3 numbers without using temporary variable


x,y,z=1,2,3
x,y,z=z,y,x
print(x,y,z)

a,b,c=10,20,30
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print(a,b,c)
'''

'''
to create Student mark list using dictionary and
find the average of every student

d1={'A':100,'B':800,'C':90}
s=d1.values()
print((sum(s))/len(d1))
'''

'''
to do arithmetic operation using function

def f(a,b):
   sum = a + b
   return sum
   
num1 = 5
num2 = 6
print(f(num1, num2))
'''

'''
to find odd numbers in the given integer list using filter() method
'''
l1 = [1,2,3,4,5]  
odd = lambda x: x % 2 != 0
l2 =set(filter(odd, l1)) 
print(l2)
