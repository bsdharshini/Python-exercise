t1=(('M',10),('A',100),('C',20))
t2=(('Q',100),('M',50),('A',500))
print("original tuple1: ",t1,"\n")
print("original tuple2: ",t2,"\n")
t1=list(t1)
t2=list(t2)
i,j=0,0
n1=len(t1)-1
n2=len(t2)-1
for i in range(0,n1):
    for j in range(0,n2):
        if(t1[i][0])==(t2[j][0]):
            if(t1[i][1]<t2[j][1]):
                del t2[j]
                
            elif(t1[i][1]>t2[j][1]):
                del t1[i]
            
t3=t1+t2
t4=(sorted(t3, key=lambda x:int(x[1] )))
t4=tuple(t4)
print("sorted and unique value tuple: \n ",t4)
