# Funciones para las operaciones
def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "No se puede dividir por cero"

# Ciclo 
while True:
    # Menú de opciones
    print("\nSeleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    # Pedir a la persona que elija una operación
    opcion = input("Ingrese el número de la operación (1/2/3/4/5): ")

    if opcion == '5':
        print("Saliendo de la calculadora. ¡Hasta luego!")
        break  # Sale del bucle y termina el programa

    # Solicita el número a las personas 
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    # Realizar la operación seleccionada
    if opcion == '1':
        print(f"{num1} + {num2} = {sumar(num1, num2)}")
    elif opcion == '2':
        print(f"{num1} - {num2} = {restar(num1, num2)}")
    elif opcion == '3':
        print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
    elif opcion == '4':
        print(f"{num1} / {num2} = {dividir(num1, num2)}")
    else:
        print("Opción no válida, por favor ingrese una opción correcta.")
