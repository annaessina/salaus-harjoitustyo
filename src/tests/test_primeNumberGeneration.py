#This is just beginning skeleton of unittest of primeNumberGeneration().
#This test will be expanded as work-in-progress.
#Tested: works fine.

import unittest
from main import primeNumberGeneration
from main import checkIfPrimeNumber

class TestPrimeNumberGeneration(unittest.TestCase):
    def test_primeNumberGeneration(self):
        #Test primeNumberGeneration function
        self.assertAlmostEqual(checkIfPrimeNumber(primeNumberGeneration(2, 20)), True)
