
def Ahorcado(index_palabras):
    plabras= ['hola', ' ahorcado', 'programar', 'computadora', 'ambato']
    
    Adivina = set()
    errores = set()
    intentos = 6

    while intentos > 0:
        display = ''.join([letter if letter in Adivina else '_' for letter in index_palabras])
        print(f"\nWord: {display}")
        print(f"Wrong guesses: {', '.join(errores) if errores else 'None'}")
        print(f"Attempts left: {intentos}")
     