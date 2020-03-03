# 第一行 2 个整数 n 和 m，表示数字个数和询问次数。
# 第二行 n 个整数，表示这些待查询的数字。
# 第三行 m 个整数，表示询问这些数字的编号，从 1 开始编号。




x = input().split()
n, m = int(x[0]), int(x[1])
y = input().split()#n个整数
z = input().split()#m个整数
num = []
res = []
for i in range(n):
    p = int(y[i])
    num.append(p)

for i in range(m):
    q = int(z[i])
    for j in range(n):
        if q==num[j] & q!=num[j-1]:
            res.append(j)
        else:
            res.append(-1)
res = list(set(res))
print(res)

