# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en
# pantalla la suma de todos los enteros desde 1 hasta N.

# Solicitar al usuario un entero positivo N
N = int(input("Introduce un entero positivo N: "))

# Verificar si el número ingresado es positivo
if N <= 0:
    print("Por favor, introduce un entero positivo.")
else:
    # Calcular la suma de los enteros desde 1 hasta N
    suma = (N + 1)*N/2

    # Mostrar la suma en pantalla
    print(suma)