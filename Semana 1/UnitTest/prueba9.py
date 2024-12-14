from ejercicio import even_numbers
import unittest

class pruebapares(unittest.TestCase):
    
    def test_1(self):
        resultado = even_numbers([1,2,3,4])
        self.assertEqual(resultado, [2,4])

if __name__ == '__main__':
    unittest.main()