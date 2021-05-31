for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=[]
    for i in range(n):
        a.append(l[i]%3)
    z=a.count(0)
    o=a.count(1)
    t=a.count(2)
    if z==0 and o!=0 and t!=0:
        print('NO')
    elif z==0 and t==0 and o!=0:
        print('YES')
    elif z==0 and o==0 and t!=0:
        print('YES')
    elif z<=(t+o):
        print('YES')
    else:
        print('NO')
