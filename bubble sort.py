#using for loop
def sort(n):
    for i in range(len(n)-1,0,-1):
        for j in range(i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
num=[5,1,2,10,4]
sort(num)
print(num)

    
