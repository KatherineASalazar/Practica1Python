#Escribir un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el
#último año y almacene ese número en una variable. A continuación, mostrar en pantalla un valor de
#verdad (True o False - tipo de datos booleanos) que indique si el usuario ha visto más de 3 shows

# Solicitar al usuario la cantidad de shows musicales vistos
cantidad_shows = int(input("Ingrese cuántos shows musicales ha visto en el último año: "))

# Verificar si ha visto más de 3 shows
ha_visto_mas_de_3 = cantidad_shows > 3

print(ha_visto_mas_de_3)