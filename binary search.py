'''#using while loop
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2
        if list[mid]== n:
            globals()['pos']=mid
            return True
        else:
            if n>list[mid]:
                l=mid+1
            else:
                u=mid-1
    return False
l1=(1,2,3,100,104,500)
n=104
if search(l1,n):
    print("{} is found at postion {}".format(n,pos))
else:
    print("Not found")
'''
# using for loop
pos=-1
def search(list,n):
    l=0
    u=len(list)-1
    for i in range(l,u):
        mid=(l+u)//2
        if list[mid]== n:
            globals()['pos']=mid
            return True
        else:
            if n>list[mid]:
                l=mid+1
            else:
                u=mid-1
    return False
l1=(1,2,3,100,104,500)
n=104
if search(l1,n):
    print("{} is found at postion {}".format(n,pos))
else:
    print("Not found")
