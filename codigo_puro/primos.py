n = int(input("Digite n: "))
flag = 0
i = 2

while(i < n):
    if(n % i == 0):
        flag = 1
        n -= 1
        i = 2
    else:
        flag = 0
    i += 1
if(flag == 0):
    print(f"O primo mais proximo de n: {n}")
    