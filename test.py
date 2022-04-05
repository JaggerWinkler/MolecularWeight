#testing file for calculator
#not needed for function
#Overkill for program

import unittest
import main

class TestCalc(unittest.TestCase):
    def test_Sodium_Cholride (self):
        self.assertEqual(main.getWeight("Na Cl", 4), 58.44)
    #def test_Rounding(self):
     #   self.assertEqual(main.getWeight("O", 4))
        
if __name__ == '__main__':
    unittest.main()