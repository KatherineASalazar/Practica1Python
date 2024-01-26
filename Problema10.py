# Escriba un programa para imprimir una lista específica después de eliminar los elementos que se
# encuentran en la posición 0, 4 y 5.
# lista de muestra: ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
# Resultado esperado: ['Verde', 'Blanco', 'Negro']

# Definir la lista de muestra
lista_muestra = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']

# Eliminar los elementos en las posiciones 0, 4 y 5
posiciones_a_eliminar = [0, 4, 5]

# Crear una nueva lista sin los elementos en las posiciones especificadas
lista_resultado = [valor for i, valor in enumerate(lista_muestra) if i not in posiciones_a_eliminar]

# Mostrar el resultado esperado
print(lista_resultado)