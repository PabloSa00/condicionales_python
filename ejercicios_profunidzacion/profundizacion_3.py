# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

temp_1 = float(input('Ingrese la primera temperatura:\n'))

temp_2 = float(input('Ingrese la segunda temperatura:\n'))

temp_3 = float(input('Ingrese la tercera temperatura:\n'))

prom = (temp_1 + temp_2 + temp_3) / 3

sentece_1 = f'La T° {temp_1:.2f} es la mayor de las tres'
sentece_2 = f'La T° {temp_2:.2f} es la mayor de las tres'
sentece_3 = f'La T° {temp_3:.2f} es la mayor de las tres'

sentece_4 = f'La T° {temp_1:.2f} es la menor de las tres'
sentece_5 = f'La T° {temp_2:.2f} es la menor de las tres'
sentece_6 = f'La T° {temp_3:.2f} es la menor de las tres'

if temp_1 > temp_2:
    if temp_1 > temp_3:
        print(sentece_1)
if temp_2 > temp_1:
    if temp_2 > temp_3:
        print(sentece_2)
if temp_3 > temp_2:
    if temp_3 > temp_1:
        print(sentece_3)

if temp_1 < temp_2:
    if temp_1 < temp_3:
        print(sentece_4)
if temp_2 < temp_1:
    if temp_2 < temp_3:
        print(sentece_5)
if temp_3 < temp_2:
    if temp_3 < temp_1:
        print(sentece_6)
    

print(f'El promedio de las T° es {prom:.2f}')