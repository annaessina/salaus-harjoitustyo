
#This is just beginning skeleton of unittest of decrypt().
#This test will be expanded as work-in-progress.

import unittest
from main import decrypt

class TestDecrypt(unittest.TestCase):
    def test_decrypt(self):
        #Test decrypt function
        self.assertAlmostEqual(decrypt(test_message), test_message_decrypted)
