
# contador de palabras de un texto.




def contador_palabras(texto):
    
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    print(f'la cantidad de palabras contadas en el texto son: {cantidad_palabras}')

contador_palabras('hola, como estas amigo, tanto tiempo sin vernos, manana tenemos el trabajo de ciencias, espero que te encunetres espectacular con los estudios, nos vemos el semestre que viene')
