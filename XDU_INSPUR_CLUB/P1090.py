# 例如有 33 种果子，数目依次为 1 ， 2 ， 9 。可以先将1 、 2 堆合并，
# 新堆数目为 3 ，耗费体力为 3 。接着，将新堆与原先的第三堆合并，又得到新的堆，
# 数目为 12 ，耗费体力为 12 。所以多总共耗费体力 =3+12=15 。
# 可以证明 15 为最小的体力耗费值。

# n = 3
# list = [1,2,9]
n = int(input())
list = input().split()

list2 = []
ans = 0
for i in range(n):
    p = int(list[i])
    list2.append(-p)
list2 = sorted(list2)

while len(list2) > 1:
    q = list2[-1]
    list2.pop()
    q += list2[-1]
    list2.pop()
    list2.append(q)
    ans -= q
    
    
print(ans)

