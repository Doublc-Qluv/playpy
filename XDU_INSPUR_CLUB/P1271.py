n = 5
m = 10
list = [2,5,2,2,5,2,2,2,1,2,6] # 2 5 2 2 5 2 2 2 1 2

x = input().split()
n = int(x[0])
m = int(x[1])
list = input().split()
list2 = []

for i in range(m):
    p = int(list[i])
    if p>=1 & p<=n:
        list2.append(p)
list2 = sorted(list2)
#print(list2)
print(*list2,sep = ' ')


'''
x = input().split()
n = int(x[0])
m = int(x[1])
list = input().split()
list2 = []
for i in range(m):
    p = int(list[i])
    if p>=1 & p<=n:
        list2.append(p)

quick_sort = lambda array: array if len(array) <= 1 else quick_sort([
    item for item in array[1:] if item <= array[0]
    ]) + [array[0]] + quick_sort([item for item in array[1:] if item > array[0]])

list2 = quick_sort(list2)
print(*list2,sep = ' ')
'''