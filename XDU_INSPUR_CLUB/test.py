# # P2240  
# N = 2
# T = 50
# ratios = []

# for i in range(N):
#     coin = input().split()
#     ratio = int(coin[1])/int(coin[0])
#     ratios.append(ratio)

# heavy = ratios[0]
# #print(sorted(ratios,reverse=True))
# for i in ratios:
#     if 

def quick_sort(b):
    """快速排序"""
    if len(b) < 2:
        return arr
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = arr[len(b) // 2]
    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    b.remove(mid)
    for item in b:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)


x = input().split()
n = int(x[0])
m = int(x[1])
list = input().split()
list2 = []
for i in range(m):
    p = int(list[i])
    if p>=1 & p<=n:
        list2.append(p)

list2 = quick_sort(list2)
print(*list2,sep = ' ')