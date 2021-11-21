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
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

numero_3 = int(input('Ingrese el tercer número:\n'))

#Solicitados los 3 numeros

sentece = f'El numero {numero_1} es par'
sentece_2 = f'El numero {numero_2} es par'
sentece_3 = f'El numero {numero_3} es par'

sentece_4 = f'El numero {numero_1} es impar'
sentece_5 = f'El numero {numero_2} es impar'
sentece_6 = f'El numero {numero_3} es impar'

if numero_1 % 2 == 0:
    print(sentece)
elif numero_1 == 0:
    print(sentece)
else:
    print(sentece_4)

if numero_2 % 2 == 0:
    print(sentece_2)
elif numero_2 == 0:
    print(sentece_2)
else:
    print(sentece_5)

if numero_3 % 2 == 0:
    print(sentece_3)
elif numero_3 == 0:
    print(sentece_3)
else:
    print(sentece_6)