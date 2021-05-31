'''
1) Ask user to give name and marks of 10 different students.
Store them in dictionary.

d={}
for i in range(2):
    name=input()
    d[name]=int(input())
    
for i,j in d.items():
    print(i,"-",j)#key and value
print((sum(d.values()))/(len(d)))#avg of value
print(d.items())#display both key and value
print(d.values())#display value
print(d.keys())#display key
for i in d.keys():
    print(i,end=" ")
d['dhara']=100 #add key and value
d['dhara']=200#updating value
del d['dhara']
print(d)#display dict 
'''
'''
2) Sort the dictionary created in previous example according to marks

d={}
for i in range(2):
    mark=int(input())
    d[mark]=input()

for i in sorted(d):
    print(i,"-",d[i])#key and value
'''   
'''
3) Use dictionary to store antonyms of words. E.g.- 'Right':'Left','Up':'Down',etc.
Display all words and then ask user to enter a word and display antonym of it.

d={'Right':'Left','Up':'Down'}
an=input()
if an in d.keys():
    print(d[an])
else:
    print('enter word in dict: ',d.keys())
'''

'''
4) Count the number of occurrence of each letter in word "MISSISSIPPI".
Store count of every letter with the letter in a dictionary.

5) From the previous question, sort according to the number of letters.

count={}
s="MISSISSIPPI"
for i in s:
    if i in count:
        count[i]+=1
    else:
        count[i]=1

for i in sorted(count.values()):
    print(i)
'''
'''
Take a list containg only strings. Now, take a string input from user and
rearrange the elements of the list according to the number of occurence of the
string taken from user in the elements of the list.

E.g.-LIST : ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug
buggy"]
STRING TAKEN : "bug"

OUTPUT LIST:["bug bun bug bun bug bug","buggy bug bug buggy",
"bunny bug","no bun"]
'''
a = ["no bun","bug bun bug bun bug bug","bunny bug","buggy bug bug buggy"]
b = "bug"
c = {}
for i in a:
  count = 0
  for j in i.split():
    if j == b:
      count = count+1
  c[count]=i
d = []
for s in sorted(c):
  d.append(c[s])
d.reverse()
print (d)


