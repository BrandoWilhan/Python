i = 0
numero = []

while (i < 5):
    numero.append(int(input(f"digite o numero {i+1}: "))) 
    i += 1

maior = numero[0]
menor = numero[0]

for x in numero:
    if(maior < x):
        maior = x
    if(menor > x):
        menor = x

print(f"esse e o menor: {menor}")
print(f"esse e o maior: {maior}")