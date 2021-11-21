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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = int(input('Ingrese el primer número:\n'))

numero_2 = int(input('Ingrese el segundo número:\n'))

#Solicitados los dos numeros

sentece = f'Calculando la diferencia entre {numero_1} y {numero_2}...'

print(sentece)

#Oracion para darle mas presentabilidad

calculo = numero_1 / numero_2

sentece_2 = f'{calculo} es un numero positivo'
sentece_3 = f'{calculo} es un numero negativo'
sentece_4 = f'{calculo} es un numero igual a cero'

if calculo < 0:
    print(sentece_3)
elif calculo > 0:
    print(sentece_2)
elif calculo == 0:
    print(sentece_4)

#Resolucion del enunciado