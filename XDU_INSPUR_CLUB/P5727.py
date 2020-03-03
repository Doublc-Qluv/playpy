list = []
x = 20
list.append(x)
while x!=1:
    # list.append(x)
    if x % 2 == 0:
        x = x / 2
        list.append(x)
    if x % 2 == 1:
        x = 3*x + 1
        list.append(x)
list.append(x)

print(listy)