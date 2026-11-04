import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # def test_add(self):
    #     self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    # ---------------- Add ------------------------
    def test_add1(self):
        self.assertEqual(self.calc.add(5,7), 12)
    def test_add2(self):
        self.assertEqual(self.calc.add(10,16), 26)
    #------------------ Sub -----------------------
    def test_sub1(self):
        self.assertEqual(self.calc.subtract(53,11), 42)
    def test_sub2(self):
        self.assertEqual(self.calc.subtract(5,-14), 19)
    #------------------ multi ---------------------
    def test_multi1(self):
        self.assertEqual(self.calc.multiply(5,-3), -15)
    def test_multi2(self):
        self.assertEqual(self.calc.multiply(3,0), 0)
    def test_multi3(self):
        self.assertEqual(self.calc.multiply(-3,-3), 9)
    #------------------ div -----------------------
    def test_div1(self):
        self.assertEqual(self.calc.divide(3,0), ValueError)
    def test_div2(self):
        self.assertEqual(self.calc.divide(-15,3), 0)
    #------------------ mod -----------------------
    def test_mod1(self):
        self.assertEqual(self.calc.modulo(10,-2), -2)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(0,2), 0)
    def test_mod2(self):
        self.assertEqual(self.calc.modulo(21,0), 0)



if __name__ == '__main__':
    unittest.main()
