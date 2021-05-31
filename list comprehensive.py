x, y, z, n = (int(input()) for a in range(4))
#x,y,z,n=map(int,input('enter vals with spaces').split(" "))
# to get input in single line
print([[i,j,k]for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=0])