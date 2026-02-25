import random
#integracion de los string 
def juego_del_ahorcado():
    # creacion de la lista
    palabras = ["python", "programacion", "computadora", "desarrollo", "codigo"]
    palabra = random.choice(palabras).upper()
    letras_adivinadas = set()
    intentos = 6
    
    print("¡Bienvenido al Juego del Ahorcado!")
    print(f"La palabra tiene {len(palabra)} letras")
    # comnienza el juego/bucle 
    while intentos > 0:
        palabra_actual = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra])
        print(f"\nPalabra: {palabra_actual}")
        print(f"Intentos restantes: {intentos}")
        print(f"Letras usadas: {', '.join(sorted(letras_adivinadas))}")
        
        if palabra_actual == palabra:
            print(f"\n¡Ganaste! felicidades La palabra era: {palabra}")
            return
        
        letra = input("Adivina una letra: ").upper()
        
        if letra in letras_adivinadas:
            print("Ya probaste esa letra")
            continue
        
        letras_adivinadas.add(letra)
        
        if letra not in palabra:
            intentos -= 1
            print("¡Letra incorrecta!")
        else:
            print("¡Letra correcta!")
    
    print(f"\n¡Perdiste! La palabra era: {palabra}")

juego_del_ahorcado()grama.
    


