"""
Nombre: Karylle Zia Legada
Fecha: Fecha: 16 de Agosto del 2023
Encriptar. Diseñe una función encripta(s, clave), que reciba un string s con un mensaje y un string con una clave de
codificación, y retorne el mensaje codificado según la clave leída. Los signos de puntuación y dígitos que aparecen
en el mensaje deben conservarse sin cambios.

La clave consiste en una sucesión de las 26 letras minúsculas del alfabeto, las cuales se hacen corresponder con el
alfabeto básico (a...z, sin la ñ o vocales acentuadas) de 26 letras. La primera letra de la clave se relaciona con
la letra 'a', la segunda con la letra 'b', etc. Por ejemplo, una entrada de la forma:

Clave = 'ixmrklstnuzbowfaqejdcpvhyg'
Texto para codificar: 'cafe'

Con esta clave la letra 'i' se corresponde con la letra 'a', la letra 'x' se corresponde con la letra 'b', la letra 'm'
se corresponde con la letra 'c', y así sucesivamente, por lo que el ejemplo anterior debería dar como salida: 'milk'.

Nota: para simplificar consideraremos solo mensajes de entrada en minúsculas.
Ejemplos:

encripta('cafe', ' ixmrklstnuzbowfaqejdcpvhyg')
'milk'

encripta('dame 1 chocolate', ' ixmrklstnuzbowfaqejdcpvhyg')
 'riok 1 mtfmfbidk'

"""
def encriptar(palabra, clave):
    abc = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for caract in palabra:
        if caract in abc:
            index = abc.index(caract)
            res += clave[index]
        else:
            res += caract
    return res

print(encriptar("cafe",'ixmrklstnuzbowfaqejdcpvhyg' ))


def encripta(texto, clave):
    abc = "abcdefghijklmnopqrstuvwxyz"
    codificacion = {abc[i]: clave[i] for i in range(26)}

    mensaje_codificado = ""
    for caracter in texto:
        if caracter in abc:
            mensaje_codificado += codificacion[caracter]
        else:
            mensaje_codificado += caracter

    return mensaje_codificado


clave = 'ixmrklstnuzbowfaqejdcpvhyg'
texto = 'cafe'
texto_codificado = encripta(texto, clave)
print(texto_codificado)


