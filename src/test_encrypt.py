
#This is just beginning skeleton of unittest of encrypt().
#This test will be expanded as work-in-progress.

import unittest
from main import encrypt

class TestEncrypt(unittest.TestCase):
    def test_encrypt(self):
        #Test encrypt function
        self.assertAlmostEqual(encrypt(test_message), test_message_encrypted)
