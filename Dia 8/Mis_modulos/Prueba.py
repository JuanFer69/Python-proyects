import cambia_texto
import unittest

class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'hola'
        resultado = cambia_texto.todo_mayuculas(palabra)
        self.assertEqual(resultado, 'HOLA')

if __name__ == 'main':
    unittest.main()