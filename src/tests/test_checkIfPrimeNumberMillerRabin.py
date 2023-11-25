#This is just beginning skeleton of unittest of checkIfPrimeNumberMillerRabin().
#This test will be expanded as work-in-progress.

import unittest
from main import checkIfPrimeNumberMillerRabin

class TestCheckIfPrimeNumberMillerRabin(unittest.TestCase):
    def test_checkIfPrimeNumberMillerRabin(self):
        #Test checkIfPrimeNumberMillerRabin function
        self.assertAlmostEqual(checkIfPrimeNumberMillerRabin(17), True)
