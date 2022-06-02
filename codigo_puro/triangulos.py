 
lista = []

lista = input().split(" ")

lista = sorted(lista, key = float, reverse = True)

A = float(lista[0])
B = float(lista[1])
C = float(lista[2])

if(A >= B + C):
    print("NAO FORMA TRIANGULO")
    
elif(pow(A,2) == pow(B, 2) + pow(C, 2)):
    print("TRIANGULO RETANGULO")

elif(pow(A,2) > pow(B, 2) + pow(C, 2)):
    print("TRIANGULO OBTUSANGULO")

elif(pow(A,2) < pow(B, 2) + pow(C, 2)):
    print("TRIANGULO ACUTANGULO")

if(A == B and B == C):
    print("TRIANGULO EQUILATERO")

if((A == B and C != A) or (B == C and A != B) or (A == C and B != A)):
    print("TRIANGULO ISOCELES")