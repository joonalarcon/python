

def maximo_minimo():
    
    lista_numeros = [ ]
    seguir_con_loop = 1

    while seguir_con_loop == 1:

        numero = input('ingrese un numero: ')
        print(f'el numero es {numero}')

        lista_numeros.append(numero)

        print(f'La lista de numeros es: {lista_numeros}')

        seguir_con_loop = int(input('Desea seguir agregando numeros? 1:Si  2:No  = '))
        
    lista_numeros.sort()
    print(f'La lista de numeros ordenadas es: {lista_numeros}')

maximo_minimo()
