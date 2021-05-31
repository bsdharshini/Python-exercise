name=input()
l=[]
for i in name:
    if i not in l:
        l.append(i)
    else:
        print(i)
