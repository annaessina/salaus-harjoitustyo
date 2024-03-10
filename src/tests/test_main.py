import unittest
from calculate_gcd import calculate_gcd
from calculateD import calculateD
from checkIfPrimeNumber import checkIfPrimeNumber
from checkIfPrimeNumberMillerRabin import checkIfPrimeNumberMillerRabin
from primeNumberGeneration import primeNumberGeneration

class TestCalculateGCD(unittest.TestCase):
    def test_calculate_gcd(self):
        #First large prime number for testing is Mersenne prime number M(1279) i.e 2**1279 - 1, which is 386 digits long
        primeM1279 = 10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087
        #Second large prime number for testing is Mersenne prime number M(2203) i.e 2**2203 - 1, which is 684 digits long
        primeM2203 = 1475979915214180235084898622737381736312066145333169775147771216478570297878078949377407337049389289382748507531496480477281264838760259191814463365330269540496961201113430156902396093989090226259326935025281409614983499388222831448598601834318536230923772641390209490231836446899608210795482963763094236630945410832793769905399982457186322944729636418890623372171723742105636440368218459649632948538696905872650486914434637457507280441823676813517852099348660847172579408422316678097670224011990280170474894487426924742108823536808485072502240519452587542875349976558572670229633962575212637477897785501552646522609988869914013540483809865681250419497686697771007
        self.assertEqual(calculate_gcd(2013, 13179), 3)
        self.assertEqual(calculate_gcd(0, 7), 7)  
        self.assertEqual(calculate_gcd(15, 0), 15)  
        self.assertEqual(calculate_gcd(0, 0), 0)
        self.assertEqual(calculate_gcd(21, 14), 7)  
        self.assertEqual(calculate_gcd(121, 114), 1)  
        self.assertEqual(calculate_gcd(primeM1279, primeM2203), 1)

class TestCalculateD(unittest.TestCase):
    def test_calculateD(self):
        e, phi, d = 5, 12, 5  
        self.assertEqual(calculateD(e, phi), d)
        self.assertEqual(calculateD(3, 10), 7)  
        self.assertEqual(calculateD(5, 16), 13)  
        self.assertEqual(calculateD(7, 20), 3)
        self.assertEqual(calculateD(11, 16), 3)  
        self.assertEqual(calculateD(73, 120), 97)  

class TestCheckIfPrimeNumber(unittest.TestCase):
    def test_checkIfPrimeNumber(self):
        #First prime number for testing is Mersenne prime number M(1279) i.e 2**1279 - 1, which is 386 digits long
        self.assertTrue(checkIfPrimeNumberMillerRabin(10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087))
        self.assertFalse(checkIfPrimeNumber(10))  
        self.assertTrue(checkIfPrimeNumber(2))  
        self.assertFalse(checkIfPrimeNumber(1))  
        self.assertTrue(checkIfPrimeNumber(17))  
        self.assertTrue(checkIfPrimeNumber(997))  

class TestCheckIfPrimeNumberMillerRabin(unittest.TestCase):
    def test_checkIfPrimeNumberMillerRabin(self):
        #First large prime number for testing is Mersenne prime number M(1279) i.e 2**1279 - 1, which is 386 digits long
        primeM1279 = 10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087
        #Second large prime number for testing is Mersenne prime number M(2203) i.e 2**2203 - 1, which is 684 digits long
        primeM2203 = 1475979915214180235084898622737381736312066145333169775147771216478570297878078949377407337049389289382748507531496480477281264838760259191814463365330269540496961201113430156902396093989090226259326935025281409614983499388222831448598601834318536230923772641390209490231836446899608210795482963763094236630945410832793769905399982457186322944729636418890623372171723742105636440368218459649632948538696905872650486914434637457507280441823676813517852099348660847172579408422316678097670224011990280170474894487426924742108823536808485072502240519452587542875349976558572670229633962575212637477897785501552646522609988869914013540483809865681250419497686697771007
        self.assertFalse(checkIfPrimeNumberMillerRabin(10))
        self.assertTrue(checkIfPrimeNumberMillerRabin(23))  
        self.assertFalse(checkIfPrimeNumberMillerRabin(1001))  
        self.assertTrue(checkIfPrimeNumberMillerRabin(7919))
        # Mersenne prime number M(1279) i.e 2**1279 - 1 is tested.
        self.assertTrue(checkIfPrimeNumberMillerRabin(primeM1279))
        # Mersenne prime number M(2203) i.e 2**2203 - 1 is tested
        self.assertTrue(checkIfPrimeNumberMillerRabin(primeM2203))
        # Multiplication of two Mersenne prime numbers M(1279) and M(2203) is tested. The result of multiplication is not a prime number.
        # Since this number is too large, it may take up to few minutes to peform this test.
        self.assertFalse(checkIfPrimeNumberMillerRabin(primeM1279*primeM2203))

class TestPrimeNumberGeneration(unittest.TestCase):
    def test_primeNumberGeneration(self):
        result1 = primeNumberGeneration(2**1023, 2**1024)
        self.assertTrue(checkIfPrimeNumberMillerRabin(result1))
        result2 = primeNumberGeneration(50, 100)  
        self.assertTrue(checkIfPrimeNumberMillerRabin(result2))
        result3 = primeNumberGeneration(10000, 20000)  
        self.assertTrue(checkIfPrimeNumberMillerRabin(result3))
