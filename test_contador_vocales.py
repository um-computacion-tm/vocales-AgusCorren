import unittest
def contar_vocales(mi_string):
    mi_string = mi_string.lower()
    for letra in mi_string:
        if letra not in 'aeiou':
            mi_string.replace(letra, "")
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado


class TestContadorVocales(unittest.TestCase):

    def test_contar_a(self):
        resultado = contar_vocales('cas')
        self.assertEqual(resultado, {'a': 1})

    def test_contar_aa(self):
        resultado = contar_vocales('casa')
        self.assertEqual(resultado, {'a': 2})

    def test_contar_bese(self):
        resultado = contar_vocales('bese')
        self.assertEqual(resultado, {'e': 2})

    def test_contar_besa(self):
        resultado = contar_vocales('besa')
        self.assertEqual(resultado, {'a': 1, 'e': 1})

    def test_contar_casanova(self):
        resultado = contar_vocales('casanova')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_mUrciElago(self):
        resultado = contar_vocales('mUrciElago')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})


if __name__ == '__main__':
    unittest.main()


'''
activado = True
while activado==True:
    palabra = input('Ingrese palabra: ')
    print(contar_vocales(palabra))

    seguir = input('¿Desea continuar? Si/No: ')
    seguir.lower
    if seguir == "si":
        continue
    else:
        activado = False
'''