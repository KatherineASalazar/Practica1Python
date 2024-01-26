# Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
# encuentran en la posición 0, 4 y 5.
# lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Resultado esperado: ['Verde', 'Blanco', 'Negro']

# Definir la lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar los elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]

for posicion in sorted(posiciones_a_eliminar, reverse=True):
    if 0 <= posicion < len(lista_muestra):
        lista_muestra.pop(posicion)

# Mostrar el resultado esperado
print("Resultado esperado:", lista_muestra)