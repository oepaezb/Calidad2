from ejercicio import is_even
import unittest

class pruebabooleanpar(unittest.TestCase):
    
    def test_1(self):
        resultado = is_even(4)
        self.assertEqual(resultado, 1)

if __name__ == '__main__':
    unittest.main()