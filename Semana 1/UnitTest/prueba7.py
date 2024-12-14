from ejercicio import remove_letter
import unittest

class pruebaquitandoletra(unittest.TestCase):
    
    def test_1(self):
        resultado = remove_letter("a","quitando la letra a")
        self.assertEqual(resultado, "quitndo l letr ")

if __name__ == '__main__':
    unittest.main()