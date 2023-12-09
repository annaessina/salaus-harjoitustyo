#This is just beginning skeleton of unittest of calculate_gcd() function.
#This test will be expanded as work-in-progress.

import unittest
from main import calculate_gcd

class TestCalculate_gcd(unittest.TestCase):
    def test_calculate_gcd(self):
        #Test calculate_gcd() function
        self.assertAlmostEqual(calculate_gcd(2013, 13179), 3)
