# En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
# restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
# porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
# dejar como propina.

costo_de_comida = float(input("¿cuánto fue el consumo en el restaurante?"))

porcentaje_propina = float(input("¿qué porcentaje de propina le dejará al mesero?"))

propina = porcentaje_propina*costo_de_comida/100

print(propina)

