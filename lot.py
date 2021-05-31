''''
import random
lotteryTicket=[1001,1002,1003,1004,1005]
name=["Abc","Bcd","Cde","Def","Efg"]
priceAmount=[0,10,100,1000,10000,100000,200000]
genTicket=0
length=len(lotteryTicket)
while genTicket<length:
    rand=random.randint(0,len(lotteryTicket)-1)
    rand1=random.randint(0,len(priceAmount)-1)
    if priceAmount[genTicket]<10000:
        print("Lottery Code: "+str(lotteryTicket[rand])+" Name is "+name[rand]+" Price amount: "+str(priceAmount[rand1]),end="\n")
    genTicket+=1
    
        
    '''    
        


import random as r
id = [1001,1002,1003,1004]
names  = ['dhara' ,'shannu' ,'nishan','nisha']
Amount= [10,100,1000,10000,10000,1000000]
id1 = r.randint(0,len(id)-1)
id2 = r.randint(0,len(id)-1)
a1 = r.randint(0,len(Amount)-1)
a2 = r.randint(0,len(Amount)-1)
c=0

while a1 == a2 or id1== id2:
    a2 = r.randint(0,len(Amount)-1)
    id2= r.randint(0,len(id)-1)
if a1<a2:
    a1,a2=a2,a1
 




print("Today's First Winner")
print('-------------------')
print('ID :',id[id1])
print('NAME :',names[id1])
print('CASH AMOUNT :',Amount[a1])




print("Today's Second Winner")
print('-------------------')
print('ID :',id[id2])
print('NAME :',names[id2])
print('CASH AMOUNT :',Amount[a2])
