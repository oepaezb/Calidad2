from ejercicio import length
import unittest

class pruebalenght(unittest.TestCase):
    
    def test_1(self):
        resultado = length([1,2,3,4])
        self.assertEqual(resultado, "Less than 5")

if __name__ == '__main__':
    unittest.main()