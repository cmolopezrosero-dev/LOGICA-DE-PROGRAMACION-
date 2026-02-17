
def Ahorcado(index_palabras):
    plabras= ['hola', ' ahorcado', 'programar', 'computadora', 'ambato']
    
    Adivina = set()
    errores = set()
    intentos = 6

    while intentos > 0:
        display = ''.join([letter if letter in Adivina else '_' for letter in index_palabras])
        print(f"\nPalabra : {display}")
        print(f"errores: {', '.join(errores) if errores else 'ninguno'}")
        print(f"intentos que quedan: {intentos}")
        guess = input("Adivina una letra: ").lower()
         #   Se menciono que solo se requeria un total de 50%  de avanze del programa.
    
