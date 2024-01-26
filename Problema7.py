# Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
# - Mostrar una suma de los dos números
# - Mostrar una resta de los dos números (el primero menos el segundo)
# - Mostrar una multiplicación de los dos números
# - En caso de introducir una opción inválida, el programa informará de que no es correcta.


while True:
    # Solicitar al usuario dos números
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    # Mostrar el menú de opciones
    print("\nMenú:")
    print("1. Sumar los dos números")
    print("2. Restar el segundo número al primero")
    print("3. Multiplicar los dos números")
    print("4. Salir del programa")

    # Solicitar al usuario que elija una opción
    opcion = input("Elija una opción (1, 2, 3 o 4): ")

    # Realizar la operación según la opción seleccionada
    if opcion == "1":
        resultado = numero1 + numero2
        print("La suma de {} y {} es: {}".format(numero1, numero2, resultado))
    elif opcion == "2":
        resultado = numero1 - numero2
        print("La resta de {} y {} es: {}".format(numero1, numero2, resultado))
    elif opcion == "3":
        resultado = numero1 * numero2
        print("La multiplicación de {} y {} es: {}".format(numero1, numero2, resultado))