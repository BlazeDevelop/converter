import unittest
from converter import convert_currency

class TestConverter(unittest.TestCase):

    def test_convert_eur_to_usd(self):
        result = convert_currency(1, 'EUR', 'USD')
        self.assertEqual(result, 1.17)

    def test_convert_usd_to_eur(self):
        result = convert_currency(1, 'USD', 'EUR')
        self.assertEqual(result, 0.85)

    def test_convert_jpy_to_gbp(self):
        result = convert_currency(100, 'JPY', 'GBP')
        self.assertEqual(result, 0.68)

    def test_convert_gbp_to_cad(self):
        result = convert_currency(1, 'GBP', 'CAD')
        self.assertEqual(result, 1.7)

    def test_convert_negative_amount(self):
        result = convert_currency(-1, 'EUR', 'USD')
        self.assertEqual(result, -1.17)

if __name__ == '__main__':
    unittest.main()