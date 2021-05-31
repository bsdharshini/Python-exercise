top=-1
def create():
    stack=[]
    return stack
def push(stack,item):
    globals()['top']=top+1
    return(stack.append(item))
def pop(stack):
    if(isEmpty(stack)):
        print("underflow")
    return(stack.pop())
def isEmpty(stack):
    return (top==-1)
lis=[1,2,4,7]
stack=create()
for i in range(len(lis)):
    push(stack,lis[i])
c=""
for i in range(len(stack)):
    d=pop(stack)
    c=c+str(d)
    
print(list(c))
         

    
    
