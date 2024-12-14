from ejercicio import total
import unittest

class pruebasumatoria(unittest.TestCase):
    
    def test_1(self):
        resultado = total([1,2,3,4])
        self.assertEqual(resultado, 10)

if __name__ == '__main__':
    unittest.main()