from ejercicio import addit
import unittest

class pruebasuma5(unittest.TestCase):
    
    def test_1(self):
        resultado = addit(10)
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
    unittest.main()