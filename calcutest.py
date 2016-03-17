import unittest

import calculadora

class TestCalcu(unittest.TestCase):
    Calcu = calculadora.Calculadora()

    def test(self):
        self.assertEqual( TestCalcu.Calcu.sumar(2,3), 5)
        self.assertEqual( TestCalcu.Calcu.restar(12,13), -1)

if __name__ == '__main__':
    unittest.main()
