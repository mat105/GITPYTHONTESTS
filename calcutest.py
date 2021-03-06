import unittest

import calculadora

class TestCalcu(unittest.TestCase):
    Calcu = calculadora.Calculadora()

    def test(self):
        self.assertEqual( TestCalcu.Calcu.sumar(2,3), 5)
        self.assertEqual( TestCalcu.Calcu.restar(12,13), -1)
        self.assertEqual( TestCalcu.Calcu.multiplicar(2,7), 14 )
        self.assertEqual( TestCalcu.Calcu.dividir(300, 100), 3)
        self.assertEqual( TestCalcu.Calcu.dividir(5, 2.5), 2 )

if __name__ == '__main__':
    unittest.main()
