



def contador_vocales(palabra):
    vocales_encontradas = []    
    contador = 0 
    vocales = ['a', 'e', 'i', 'o', 'u']
    
    for letra in palabra:
        
        for vocal in vocales:
            if vocal == letra:
                vocales_encontradas.append(vocal)

    print(vocales_encontradas)


contador_vocales('jonathan patricio alarcon soto')
