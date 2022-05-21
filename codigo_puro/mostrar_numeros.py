def mostrar_numeros():
    ini = int(input('de onde voce quer comecar a mostrar ?\n'))
    fim = int(input('onde termina ?\n'))
    print('\n')
    
    for i in range(ini, fim + 1):
        print(i)


mostrar_numeros()


