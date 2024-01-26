#Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente
#lista. Su programa debe retornar otra lista sin los duplicados.
#Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
#Lista procesada: [1, 2, 3, 4,, 5]

# Lista original con elementos duplicados
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]

# Eliminar duplicados utilizando un conjunto
lista_procesada = list(set(lista_original))

# Mostrar la lista procesada
print("Lista original:", lista_original)
print("Lista procesada:", lista_procesada)