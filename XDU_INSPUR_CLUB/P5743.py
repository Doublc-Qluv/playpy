# 1=1
# 2=(1+1)*2
# 3=((1+1)*2 + 1) *2
n = int(input())
x = -0.5
for i in range(n):
    x = (x + 1) * 2
print(int(x))