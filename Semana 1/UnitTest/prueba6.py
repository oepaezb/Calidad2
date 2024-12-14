from ejercicio import reverse
import unittest

class pruebareversa(unittest.TestCase):
    
    def test_1(self):
        resultado = reverse("alverrez")
        self.assertEqual(resultado, "zerrevla")

if __name__ == '__main__':
    unittest.main()