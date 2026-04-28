import unittest
import dollartonaria
class TestNairaExchange(unittest.TestCase):
	def test_test_naira_exchange_exists(self):
		dollartonaira.dollar_to_naira(2.5)
	def test_test_naira_exchange_return_correct_result_with_a_float_digit(self):
		actual = nairaexchange.naira_exchange(2.5)
		expected = 1860.0
		self.assertEqual(actual, expected)
	def test_test_naira_exchange_return_correct_result_with_a_int_digit(self):
		actual = nairaexchange.naira_exchange(1)
		expected = 1550
		self.assertEqual(actual, expected)
