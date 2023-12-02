#This is just beginning skeleton of unittest of primeNumberGeneration().
#This test will be expanded as work-in-progress.

import unittest
from main import primeNumberGeneration
from main import checkIfPrimeNumberMillerRabin

class TestPrimeNumberGeneration(unittest.TestCase):
    def test_primeNumberGeneration(self):
        #Test primeNumberGeneration function
        self.assertAlmostEqual(checkIfPrimeNumberMillerRabin(primeNumberGeneration(2**1278, 2**2282)), True)
