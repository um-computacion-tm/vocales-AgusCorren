import unittest

def tildes_f(lar):
    tildes_dic = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}
    for tilde in lar:
        if tilde in 'áéíóú':
            sin_tilde = tildes_dic[tilde]
            lar = lar.replace(tilde, sin_tilde)
    return lar

def contar_vocales(mi_string):
    mi_string = mi_string.lower()
    mi_string = tildes_f(mi_string)
    vocales = ('a', 'e', 'i', 'o', 'u')
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    if resultado == {}:
        return "NO CONTIENE VOCALES"
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

    def test_contar_espacios0(self):
        resultado = contar_vocales('Pues ayer funcionaba...')
        self.assertEqual(resultado, {'a':3, 'e':2, 'i':1, 'o':1, 'u':2})

    def test_contar_espacios1(self):
        resultado = contar_vocales('Si se puede imaginar, se puede programar')
        self.assertEqual(resultado, {'a':4, 'e':6, 'i':3, 'o':1, 'u':2})

    def test_contar_tildes1(self):
        resultado = contar_vocales('cÁsá n Óva')
        self.assertEqual(resultado, {'a': 3, 'o': 1})

    def test_contar_tildes2(self):
        resultado = contar_vocales('m ú  rciÉ lagÓ')
        self.assertEqual(resultado, {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1})
        

if __name__ == '__main__':
    unittest.main()