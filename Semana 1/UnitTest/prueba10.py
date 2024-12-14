from ejercicio import odd_numbers
import unittest

class pruebaimpares(unittest.TestCase):
    
    def test_1(self):
        resultado = odd_numbers([1,2,3,4])
        self.assertEqual(resultado, [1,3])

if __name__ == '__main__':
    unittest.main()