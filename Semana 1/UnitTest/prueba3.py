from ejercicio import mult
import unittest

class pruebamultiysuma(unittest.TestCase):
    
    def test_1(self):
        resultado = mult(5)
        self.assertEqual(resultado, 50)

if __name__ == '__main__':
    unittest.main()