def gray_code(n):                                   # 递归，代码简单，速度较应用序慢
    if n == 1: return ['0','1']
    return ['0'+i for i in gray_code(n-1)] + ['1'+i for i in gray_code(n-1)[::-1]]
def gray_code_for_2(n):                                 # 循环顺序实现，速度优势
    list = ['0', '1']
    for i in range(1,n):
        left  = ['0'+i for i in list]
        right = ['1'+i for i in list[::-1]]
        list = left + right
    return list

# n=3
# m=5

x = input().split()
n = int(x[0])
m = int(x[1])
list = gray_code(n)
print(int(list[m]))