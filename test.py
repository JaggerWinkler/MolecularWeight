#testing file for calculator
#not needed for function
#Overpkill for program

from re import A
import unittest
import calculator

class TestCalc(unittest.TestCase):
    def test_Sodium_Cholride (self): 
        self.assertEqual(calculator.get_weight("Na Cl", 4), 58.44)
    def test_Rounding(self):
        self.assertEqual(calculator.get_weight("O 4", 2), 64)
        self.assertEqual(calculator.get_weight("O 4"), 63.9976)
        self.assertEqual(calculator.get_weight("O 4", 6), 63.9976)
    def test_PolyAtomics (self):
        self.assertEqual(calculator.get_weight("N H 4", 4), 18.04)
        self.assertEqual(calculator.get_weight("C 2 H 3 O 2", 4), 59.04)
        self.assertEqual(calculator.get_weight("S 2 O 3", 7), 112.1282 )
    def test_empty (self):
        self.assertWarns(UserWarning, calculator.get_weight("j"), 1)
       
def main():
    print(calculator.get_weight("N H 4", 4)) 
   
if __name__ == '__main__':
    main()
    unittest.main()
