"""
Nombre: Karylle Zia Legada
Fecha: Fecha: 16 de Agosto del 2023

 Diseña una función desencripta(s, clave) que realice la función inversa a la función anterior, es decir,
 reciba un string s y una clave y realice la desencriptación del mensaje en el string devolviendo la cadena desencriptada.

Ejemplos:

clave = ' ixmrklstnuzbowfaqejdcpvhyg'

desencripta('milk',clave)
'cafe'

desencripta('riok 1 mtfmfbidk',clave)
 'dame 1 chocolate'

"""

def desencripta(palabra, clave):
    abc = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    for caract in palabra:
        if caract in clave:
            index = clave.index(caract)
            res += abc[index]
        else:
            res += caract
    return res

print(desencripta("riok 1 mtfmfbidk",'ixmrklstnuzbowfaqejdcpvhyg' ))

