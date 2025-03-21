import random

numero_secreto = random.randint(1, 10)
while True:
    intento = int(input("Adivina el número (1-10): "))
    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        if intento > numero_secreto:
            print("el numero es menor")
        else:
            print("el numeroes mayor")