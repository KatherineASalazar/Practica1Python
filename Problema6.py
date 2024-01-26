#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere
#calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe
#preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4
#años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $5 y si es mayor de 18 años, S10.

# Solicitar al usuario la edad del cliente
edad_cliente = int(input("Ingrese la edad del cliente: "))

# Calcular el precio de entrada según la edad
if edad_cliente < 4:
    precio_entrada = 0  # Menores de 4 años entran gratis
elif 4 <= edad_cliente <= 18:
    precio_entrada = 5  # Entre 4 y 18 años pagan $5
else:
    precio_entrada = 10  # Mayores de 18 años pagan $10

# Mostrar el precio de entrada en pantalla
print(precio_entrada)