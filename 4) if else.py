#Level-1

'''
Take values of length and breadth of a rectangle from user and
check if it is square or not.

l=int(input())
b=int(input())
if(l==b):
    print("it is a square")
else:
    print("it is  not a square")
'''

'''
Take two int values from user and print greatest among them.

n1=int(input())
n2=int(input())
if(n1<n2):
    print("n2={} is greater".format(n2))
elif(n1>n2):
    print("n1={} is greater".format(n1))
'''

'''
A shop will give discount of 10% if the cost of purchased
quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user.


q=int(input("quality"))
cost=q*100
if(cost>1000):
    cost=cost-(cost*(10/100))
    print("After discount",cost)
else:
    print(cost)
  '''

'''
A company decided to give bonus of 5% to employee
if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.

s=int(input())
year=int(input())
if(year>5):
    print("New salary",s+(s*(5/100)))
else:
    print(s)
'''


'''
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.

mark=int(input())
if(mark>80):
    print("A")
elif(mark>60 and mark<=80):
    print("B")
elif(mark>50 and mark<=60):
    print("C")
elif(mark>45 and mark<=50):
    print("D")
elif(mark>25 and mark<=45):
    print("E")
elif(mark<=25):
    print("F")
'''

'''
Take input of age of 3 people by user and determine oldest and youngest among them.

a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("A is greateset")
elif(b>a and b>c):
    print("B is Greatest")
elif(c>a and c>b):
    print("C is greatest")
else:
    print("all are equal")

    '''
'''
Write a program to print absolute vlaue of a number entered by user. E.g.-
INPUT: 1        OUTPUT: 1
INPUT: -1        OUTPUT: 1

n=int(input())
if(n<0):
    n=(-1)*n
    print(n)
else:
    print(n)
'''
'''
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
    
held=int(input())
attended=int(input())
per=(attended/held)*100
print(per,"%")
if (per>75):
    print("allowed for exam")
else:
    print("not allowed for exam")
'''

'''
Modify the above question to allow student to sit if he/she has medical cause.
Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

held=int(input())
attended=int(input())
medical=input("Medicalissue: Y/N ")
per=(attended/held)*100
print(per,"%")
if (per>75):
    print("allowed for exam")
elif(per<75 and medical=='Y'):
    print("allowed for exam")
elif(per<75 and medical=='N'):
    print("not allowed for exam")
'''

#level-2
'''
Write a program to check if a year is leap year or not.
If a year is divisible by 4 then it is leap year but
if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.

year=int(input())
if(year%4)==0 and (year%100)==0 or (year%400)==0:
    print("leap year")
else:
    print("Not leap year")
'''

'''
Ask user to enter age, sex ( M or F ), marital status ( Y or N )
and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.

if employee is a male and age is in between 20 to 40 then he may work in anywhere

if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

And any other input of age should print "ERROR".

age=int(input())
sex=input("Enter the sex: M/F ")
marital=input("Enter the martial status: Y/N ")

if sex=='F':
    print("Work in urban area")
elif(sex=='M') and age>20 and age<40:
    print("Work anywhere")
elif(sex== 'M') and age>40 and age<60:
    print("Work in Urban")
else:
    print("ERROR")
'''

'''
A 4 digit number is entered through keyboard. Write a program to print a new number with digits reversed as of orignal one. E.g.-
INPUT : 1234        OUTPUT : 4321
INPUT : 5982        OUTPUT : 2895
'''
n=input()
print(n[::-1])
