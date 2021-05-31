#using for loop
'''pos=-1
def search(l,n):
    i=0
    for i in range(len(l)):
        if l[i]==n:
            globals()['pos']=i
        return True
    return False
l=[1,2,3,4,5]
n=4
if search(l,n):
    print("{} is found at {}".format(n,pos))
else:
    print("Not found")

'''
#using while loop

pos=-1
def search(l,n):
    i=0
    while i<len(l):
        if l[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False
        
 


    
    
l=(1,2,3,4)
n=3
if search(l,n):
    print("Found ",pos)
else:
    print("Not found")

        
