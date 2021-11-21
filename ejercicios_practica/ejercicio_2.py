# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
texto_1 = str(input('Ingrese la primera palabra:\n'))

texto_2 = str(input('Ingrese la segunda palabra:\n'))

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

sentece_a = f'{texto_1} es mayor alfabeticamente que {texto_2}'
sentece_b = f'{texto_2} es mayor alfabeticamente que {texto_1}'

if texto_1 > texto_2:
    print(sentece_a)
elif texto_2 > texto_1:
    print(sentece_b)
else:
    print('Las palabras ingresadas son iguales alfabeticamente')


sentece_c = f'{texto_1} tiene mas caracteres que {texto_2}'
sentece_d = f'{texto_2} tiene mas caracteres que {texto_1}'

if len(texto_1) > len(texto_2):
    print(sentece_c)
elif len(texto_2) > len(texto_1):
    print(sentece_d)
else:
    print('Las palabras ingresadas tienen igual cantidad de caracteres')


sentece_e = f"{texto_1[0]} es mayor que {texto_2[0]}"
sentece_f = f"{texto_2[0]} es mayor que {texto_1[0]}"

if texto_1[0] > texto_2[0]:
    print(sentece_e)
elif texto_2[0] > texto_1[0]:
    print(sentece_f)
else:
    print('Las letras iniciales son iguales')


sentece_1 = 'La copia y el original son iguales'
sentece_2 = 'Como es esto posible?'

if copia_texto_1 == texto_1:
    print(sentece_1)
else:
    print(sentece_2)


sentece_3 = 'Perfecto, la copia_texto_1 es distinta de texto_2'
sentece_4 = 'Error, la copia_texto_1 es igual a texto_2'

if copia_texto_1 != texto_2:
    print(sentece_3)
else:
    print(sentece_4)