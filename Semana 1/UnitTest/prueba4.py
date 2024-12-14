from ejercicio import divide
import unittest

class pruebadivicion(unittest.TestCase):
    
    def test_1(self):
        resultado = divide(4,2)
        self.assertEqual(resultado, 2)

if __name__ == '__main__':
    unittest.main()