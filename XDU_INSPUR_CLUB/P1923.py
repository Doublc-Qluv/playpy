# P1923
# num = 5
# min = 1
# list = [4, 3, 2, 1, 5]# 4 3 2 1 5

x = input().split()
num = int(x[0])
min = int(x[1])
y = input().split()
list = []
for i in range(num):
    p = int(y[i])
    list.append(p)

list2 = sorted(list)
print(list2[min])