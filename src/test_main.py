import unittest
from calculate_gcd import calculate_gcd
from calculateD import calculateD
from checkIfPrimeNumber import checkIfPrimeNumber
from checkIfPrimeNumberMillerRabin import checkIfPrimeNumberMillerRabin
from primeNumberGeneration import primeNumberGeneration

class TestCalculateGCD(unittest.TestCase):
    def test_calculate_gcd(self):
        self.assertEqual(calculate_gcd(2013, 13179), 3)
        self.assertEqual(calculate_gcd(0, 7), 7)  
        self.assertEqual(calculate_gcd(15, 0), 15)  
        self.assertEqual(calculate_gcd(0, 0), 0)  
        self.assertEqual(calculate_gcd(21, 14), 7)  
        self.assertEqual(calculate_gcd(23, 46), 23)  

class TestCalculateD(unittest.TestCase):
    def test_calculateD(self):
        e, phi, d = 5, 12, 5  
        self.assertEqual(calculateD(e, phi), d)
        self.assertEqual(calculateD(3, 10), 7)  
        self.assertEqual(calculateD(5, 16), 13)  
        self.assertEqual(calculateD(7, 20), 3)  

class TestCheckIfPrimeNumber(unittest.TestCase):
    def test_checkIfPrimeNumber(self):
        #First prime number for testing is Mersenne prime number M(1279) i.e 2**1279 - 1, which is 386 digits long
        self.assertTrue(checkIfPrimeNumberMillerRabin(
10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087))
        self.assertFalse(checkIfPrimeNumber(10))  
        self.assertTrue(checkIfPrimeNumber(2))  
        self.assertFalse(checkIfPrimeNumber(1))  
        self.assertTrue(checkIfPrimeNumber(17))  
        self.assertTrue(checkIfPrimeNumber(997))  

class TestCheckIfPrimeNumberMillerRabin(unittest.TestCase):
    def test_checkIfPrimeNumberMillerRabin(self):
        #First prime number for testing is Mersenne prime number M(1279) i.e 2**1279 - 1, which is 386 digits long
        self.assertTrue(checkIfPrimeNumberMillerRabin(
10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087))
        self.assertFalse(checkIfPrimeNumberMillerRabin(10))
        self.assertTrue(checkIfPrimeNumberMillerRabin(23))  
        self.assertFalse(checkIfPrimeNumberMillerRabin(1001))  
        self.assertTrue(checkIfPrimeNumberMillerRabin(7919))  

class TestPrimeNumberGeneration(unittest.TestCase):
    def test_primeNumberGeneration(self):
        result = primeNumberGeneration(2**1000, 2**1001)
        self.assertTrue(checkIfPrimeNumberMillerRabin(result))
        result2 = primeNumberGeneration(50, 100)  
        self.assertTrue(checkIfPrimeNumberMillerRabin(result2))
        result3 = primeNumberGeneration(10000, 20000)  
        self.assertTrue(checkIfPrimeNumberMillerRabin(result3))



 
       