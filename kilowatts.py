taxa_de_servico = 5.00
valor_total = 0

kilowatts = float(input())

if(kilowatts <= 500):
    consumo = kilowatts*0.02

elif(kilowatts > 500 and kilowatts <= 1000):
    consumo = 500*0.1 + (kilowatts - 500)*0.05

else:
    consumo = 1000*0.35 + (kilowatts -1000)*0.1

valor_total = consumo + taxa_de_servico

print(f"{consumo: .2f} {taxa_de_servico: .2f} {valor_total: .2f}")