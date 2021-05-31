'''
Write a program to print every character of a string entered by
user in a new line using loop.

s='hello'
for i in s:
    print(i)
'''
'''
Write a program to find the length of the string "refrigerator"
without using len function.

s='refrigerator'
count=0
for i in s:
    count+=1
print(count)
'''
'''
Write a program to check if the letter 'e' is present in the word 'Umbrella'.

s='Umbrella'
count=0
for i in s:
    if i=='e':
        print("yes",end=" ")
        count+=1
print(count," times")
'''
'''
Write a program to check if the word 'orange' is present in the
"This is orange juice".

print ('orange' in "This is orange juice")
#or
a="This is orange juice"
print('orange' in a.split())
'''
'''
Write a program to find the first and the last
occurence of the letter 'o' and character ',' in "Hello, World".

s="Hello,World"
count=0
for i in s:
    if i=='o':
        break
    else:
        count+=1        
print("first 'o' ",count)
count1=0
for i in s:
    if i==',':
        break
    else:
        count1+=1        
print("first ',' ",count1)
l=s[::-1]
count2=len(s)
for i in l:
    if i=='o':
        break
    else:
        count2-=1
print("last 'o' ",count2)
count3=len(s)
for i in l:
    if i==',':
        break
    else:
        count3-=1        
print("last ',' ",count3)
'''
'''
Write the string after the first occurrence of ',' and the string after
the last occurrence of ',' in the string "Hello, Good, Morning". World".

s="Hello, Good, Morning. World"
print("\'original: \'",s)
count=0
for i in s:
    if i==',':
        index=i
        break
    else:
        count+=1
        
print("\'first: \'",s[count+1:])
        
s=s[::-1]
count1=0
for i in s:
    if i==',':
        index=i
        break
    else:
        count1+=1
print("\'last:\' ",s[count1-1::-1],end="")
'''      
'''
Write a program that takes your full name as input and
displays the abbreviations of the first and middle names except the
last name which is displayed as it is.
For example, if your name is Robert Brett Roser,
then the output should be R.B.Roser.

s=input()
s=s.split()
print(s)
f_name=s[0]
m_name=s[1]
l_name=s[2]
f_name=f_name.title()
m_name=m_name.title()
l_name=l_name.title()
print("{}.{}.{}".format(f_name[0],m_name[0],l_name))
'''
'''
Write a program to find the number of vowels, consonents,
digits and white space characters in a string.

s=input()
vow=['a','e','i','o','u']
dig=['0','1','2','3','4','5','6','7','8','9']
v,c,d,w=0,0,0,0
vowel=[]
digit=[]
consonent=[]

for i in s:
    if i in vow:
        v+=1
        vowel.append(i)
    elif i.isdigit():
        d+=1
        digit.append(i)
    elif i==" ":
        w+=1
    elif i not in vow and i!=" ":
        consonent.append(i)
        c+=1
    else:
        print('not allowed')
        
print("vowel are {} and {} times occurs".format(vowel,v))
print("consonent are {} and {} times occurs".format(consonent,c))
print("digits are {} and {} times occurs".format(digit,d))
print("whitespace {} times occurs".format(w))
'''
'''
Write a program to make a new string with all the consonents
deleted from the string "Hello, have a good day".

s='Hello, have a good day'
t=''
vow=['a','e','i','o','u']
for i in s:
    if i not in vow:
        t+=i
        
        
print(t)
'''
'''
Write a program to find out the largest and smallest word in the string
"This is an umbrella".

#letter
s="this is an umbrella"
s=s.replace(" ","")
maxi=s[0]
mini=s[0]
for i in s:
    if i>maxi:
        maxi=i
    if i<mini:
        mini=i
print(maxi)
print(mini)
#word
a = "This is an umbrella"
a = a.split()
maxx = a[0]
max_len = len(a[0])
for i in a:
  if len(i)>max_len:
    max_len = len(i)
    maxx = i
print (maxx)
'''
'''
Write a program to check if a given string is a Palindrome.
A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

s='ccaacc'
t=s[::-1]
if s==t:
    print("yes")
else:
    print("No")
        
'''
'''
Write down the names of 10 of your friends in a list and
then sort those in alphabetically ascending order.
l=[]
for i in range(5):
    name=input()
    l.append(name)
print(l)
l.sort()
c=1
for i in l:
    print(c,'',i)
    c+=1
'''
'''
Write a program to make a new string with the word "the" deleted in the
sentence "This is the lion in the cage".

s="This is the lion in the cage"
s=s.split()
l=""
for i in s:
    if i=='the':
        #l+=i+" "
        del(s[s.index(i)])
        
print(' '.join(s))
'''
'''
Write a program to check if the two strings entered by user are anagrams or not.
Two words are said to be anagrams if the letters of one word can be rearranged
to form the other word. For example, jaxa and ajax are anagrams of each other.
'''
one=input()
two=input()
l=[]
m=[]
for i in one:
    l.append(i)
for j in two:
    m.append(j)
l.sort()
m.sort()
if l==m:
    print('yes')
else:
    print('no')

