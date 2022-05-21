def maior(x, y):
    if(x > y):
        return x
    else:
        return y

def media(x, y):
    return (x + y)/2

def pot(x, y):
    return x**y

x = int(input("digite o primeiro numero: "))
y = int(input("digite o segundo numero: "))

print(f"o maior e: {maior(x, y)}")
print(f"a media entre eles e: {media(x, y)}")
print(f"{x}^{y} e: {pot(x, y)}")