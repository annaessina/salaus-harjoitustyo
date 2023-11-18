#This is just beginning skeleton of unittest of calculateD().
#This test will be expanded as work-in-progress.

import unittest
from main import calculateD

class TestCalculateD(unittest.TestCase):
    def test_calculateD(self):
        #Test calculateD function
        self.assertAlmostEqual(calculateD(e, phi), d)
