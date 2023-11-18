#This is just beginning skeleton of unittest of checkIfPrime Number().
#This test will be expanded as work-in-progress.
#Tested: works fine.

import unittest
from main import checkIfPrimeNumber

class TestCheckIfPrimeNumber(unittest.TestCase):
    def test_checkIfPrimeNumber(self):
        #Test checkIfPrimeNumber function
        self.assertAlmostEqual(checkIfPrimeNumber(7), True)
