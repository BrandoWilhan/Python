lista = [0]

for x in range(3):
    lista.append(float(input())) 
    
lista.sort(reverse = True)

A = lista[0]
B = lista[1]
C = lista[2]

if(A >= B + C):
    print("NAO FORMA TRIANGULO")
    
elif(pow(A,2) == pow(B, 2) + pow(C, 2)):
    print("TRIANGULO RETANGULO")

elif(pow(A,2) > pow(B, 2) + pow(C, 2)):
    print("TRIANGULO OBTUSANGULO")

elif(pow(A,2) < pow(B, 2) + pow(C, 2)):
    print("TRIANGULO ACUTANGULO")

elif(A == B and B == C):
    print("TRIANGULO EQUILATERO")

elif((A == B and C != A) or (B == C and A != B) or (A == C and B != A)):
    print("TRIANGULO ISOCELES")