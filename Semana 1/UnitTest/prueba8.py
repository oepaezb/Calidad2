from ejercicio import max
import unittest

class pruebamax(unittest.TestCase):
    
    def test_1(self):
        resultado = max([1,2,3,4])
        self.assertEqual(resultado, 4)

if __name__ == '__main__':
    unittest.main()