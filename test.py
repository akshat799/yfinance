import unittest
from yfinance.base import TickerBase

class TickerHistoryTestCase(unittest.TestCase):
	"""Various unit tests for yfinance's base.py history function.

	https://docs.python.org/3.9/library/unittest.html
	"""
	
	def setUp(self):
		"""Set up mock TickerBase object to test its history function"""
		self.mockTickerBase = TickerBase("ABTC-USD.SW")

	def test_example_1(self):
		"""Testing if printing history returns an output"""
		history_df = self.mockTickerBase.history()

		history_string = history_df.to_string()
		print(history_string, "\n") # debugging purposes to see dataframe

		self.assertNotEqual(None, history_string) # validate non-empty dataframe

	def test_hundred_year_range(self):
		"""Testing if an error is thrown when exceeding a 100 year data range"""
		history_df = self.mockTickerBase.history(period='max')

		history_string = history_df.to_string()
		print(history_string, "\n") # debugging purposes to see dataframe

		self.assertIn("Empty DataFrame", history_string) # validate empty dataframe due to error thrown

	def test_one_minute_interval(self):
		"""Testing if an error is thrown when interval is one minute"""
		history_df = self.mockTickerBase.history(interval="1m")

		history_string = history_df.to_string()
		print(history_string, "\n") # debugging purposes to see dataframe

		self.assertIn("Empty DataFrame", history_string) # validate empty dataframe due to error thrown

if __name__ == '__main__':
	unittest.main()


		