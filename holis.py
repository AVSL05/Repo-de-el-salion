print("Hola a todos :D")
print("Esto es una prueba")

# Código básico de python

import random

def saludo():
    nombre = input("¿Cómo te llamas? ")
    print(f"¡Hola, {nombre}! Bienvenido a este pequeño programa interactivo.")

def menu():
    print("\nMenú de opciones:")
    print("1. Generar un número aleatorio")
    print("2. Calcular la suma de dos números")
    print("3. Salir")
    opcion = input("Elige una opción (1/2/3): ")
    return opcion

def numero_aleatorio():
    num = random.randint(1, 100)
    print(f"Tu número aleatorio es: {num}")

def suma():
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        print(f"La suma de {num1} y {num2} es: {num1 + num2}")
    except ValueError:
        print("Por favor, ingresa valores numéricos válidos.")

def main():
    saludo()
    while True:
        opcion = menu()
        if opcion == "1":
            numero_aleatorio()
        elif opcion == "2":
            suma()
        elif opcion == "3":
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
