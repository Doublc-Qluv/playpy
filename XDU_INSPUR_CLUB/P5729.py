#
x = input().split()
x[0],x[1],x[2] = int(x[0]),int(x[1]),int(x[2])
V = x[0] * x[1] * x[2]
q = int(input())
if q<=100 & x[0]>=1 & x[1]<20 & x[2]<20:
    for i in range(q):
        y = input().split()
        x1,x2,x3,z1,z2,z3 = int(y[0]),int(y[1]),int(y[2]),int(y[3]),int(y[4]),int(y[5])
        V2 = (z1-x1+1) * (z2-x2+1) * (z3-x3+1)
        # if x1<=x[0] & z1<=x[0] & x2<=x[1] & z2<=x[1] & x3<=x[2] & z3<=x[2] & V > 0:
        V = V-V2
print(V)