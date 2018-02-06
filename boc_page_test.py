import unittest
from boc_page import BocPage

class BocPageTest(unittest.TestCase):

    def setUp(self):
        self.boc = BocPage()

    def test_find_popup(self):
        assert self.boc.value == 1
    
    def tearDown(self):
        pass

if (__name__ == "__main__"):
    unittest.main()