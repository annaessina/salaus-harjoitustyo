#This is just beginning skeleton of unittest of checkIfPrimeNumberMillerRabin().
#This test will be expanded as work-in-progress.

import unittest
from main import checkIfPrimeNumberMillerRabin

class TestCheckIfPrimeNumberMillerRabin(unittest.TestCase):
    def test_checkIfPrimeNumberMillerRabin(self):
        #Test checkIfPrimeNumberMillerRabin function
        #Test prime number is Mersenne prime number M(1279) which is 386 digits long
        self.assertAlmostEqual(checkIfPrimeNumberMillerRabin(10407932194664399081925240327364085538615262247266704805319112350403608059673360298012239441732324184842421613954281007791383566248323464908139906605677320762924129509389220345773183349661583550472959420547689811211693677147548478866962501384438260291732348885311160828538416585028255604666224831890918801847068222203140521026698435488732958028878050869736186900714720710555703168729087), True)
