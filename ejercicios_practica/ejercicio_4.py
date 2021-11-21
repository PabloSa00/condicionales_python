# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

texto_1 = '5'
texto_2 = '7'

# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda

# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

sentence = f'{texto_1} es mayor alfabeticamente que {texto_2}'
sentence_2 = f'{texto_2} es mayor alfabeticamente que {texto_1}'

if texto_1 > texto_2:
    print(sentence)
elif texto_2 > texto_1:
    print(sentence_2)
else:
    print('Ambos textos son iguales alfabeticamente')

numero_1 = int(texto_1)
numero_2 = int(texto_2)

sentence_3 = f'{numero_1} es mayor que {numero_2}'
sentence_4 = f'{numero_2} es mayor que {numero_1}'

if numero_1 > numero_2:
    print(sentence_3)
elif numero_2 > numero_1:
    print(sentence_4)
else:
    print('Ambos numeros son iguales')

'''Respuesta a la pregunta:
Creo que esto se debe principalmente a dos hechos:
Primero: Que analiticamente hablando, todas las letras tienen un valor numerico creciente, desde la A< hasta la >Z. 
y
Segundo:Que el ordenador es capaz de generar estas letras por codigo conformado por numeros (Ejemplo: Ä es 0196 y A es 65) '''