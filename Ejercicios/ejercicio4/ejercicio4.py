


def invertir_cadena(palabra):
    palabra_invertida = ''

    for letra in reversed(palabra):
        palabra_invertida = palabra_invertida + letra

    print(palabra_invertida)

invertir_cadena('diego alejandro alarcon soto')
