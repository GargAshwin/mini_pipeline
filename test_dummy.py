import pandas as pd
import unittest

class FlightTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv('sample.csv')

    def test_rows(self):
        self.assertGreaterEqual(len(self.df), 2)

    def test_cols(self):
        self.assertGreaterEqual(len(self.df.columns), 2)