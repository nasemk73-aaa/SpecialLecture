import unittest

from speciallecture.CSVPrinter import CSVPrinter


def setUpModule():
    print("Running setUpModule")
def tearDownModule():
    print("Running tearDownModule")
class TestCSVPrinter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Running setUpClass")
    @classmethod
    def tearDownClass(cls):
        print("Running tearDownClass")