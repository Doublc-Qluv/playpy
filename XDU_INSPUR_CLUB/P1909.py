# 57
# 2 2
# 50 30
# 30 27

n = int(input())
x1 = input().split()
x2 = input().split()
x3 = input().split()

x = x1 + x2 + x3
res = 100000000

for i in range(3):
    per = int(x[2*i+1]) / int(x[2*i])
    boxs = -(-n//int(x[2*i]) )
    price = boxs * int(x[2*i+1])
    
    if res<price:
        res = res
    else:
        res = price

print(res)