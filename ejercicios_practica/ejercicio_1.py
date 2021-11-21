# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica

# Comparadores
# Ingrese dos números cualesquiera y realice las sigueintes
# comparaciones entre ellos
numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

# Compare cual de los dos números es mayor
# Imprima en pantalla según corresponda

# Verifique si el numero_1 positivo, negativo o cero
# Imprima el resultado en cada caso

# Verifique si el numero_1 es mayor a 0 y menor a 100
# Imprima en pantalla si se cumple o no la condición

# Verifique si el numero_1 es menor a 10 o el numero_2
# es mayor a -2
# Imprima en pantalla si se cumple o no la condición

sentence_a = f'{numero_1} es mayor que {numero_2}'
sentence_b = f'{numero_2} es mayor que {numero_1}'

if numero_1 > numero_2: 
    print(sentence_a)
else:
    print(sentence_b)

sentence_c = f'{numero_1} es positivo'
sentence_d = f'{numero_1} es igual a cero'
sentence_e = f'{numero_1} es negativo'

if numero_1 > 0:
    print(sentence_c)
elif numero_1 == 0:
    print(sentence_d)
else:
    print(sentence_e)

sentence = 'Felicidades, tu numero cumple nuestra condicion (es mayor a cero y menor que cien)'
sentence_2 = 'Ups, ha habido un problema, tu numero no cumple con nuestra condición :('

if 0 < numero_1 < 100:
    print(sentence)
else:
    print(sentence_2)

sentence_3 = 'Si numero_1 es menor que 10 o numero_2 es mayor a -2, veras este mensaje'

if numero_1 < 10 or numero_2 > -2:
    print(sentence_3)
else:
    print('No se han cumplido ninguna de las condiciones')