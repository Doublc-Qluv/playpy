x = int(input())

n = 20002
p = [2]
for i in range(3,n):
    for j in range(2,int(i**0.5)+1):
        if i%j ==0:
            break
    else:
        p.append(i)
for i in p:
    for j in p:
        for k in p:
            if i+j+k == x:
                print(i,j,k)
                exit(0)