import unittest
from pokerDeuces import keyMax, calcFlopWins

class KeyMaxTests(unittest.TestCase):
	"""Tests for keyMax function"""
	
	def testIfTrue(self):
		"""Check truthiness for given dictionary"""
		testDict = {1:1, 2:2, 3:3}
		self.assertTrue(keyMax(testDict) == 3)

class CalcFlopWins(unittest.TestCase):
	"""Test for calcFlopWins function"""

	def testExceptions(self):
		"""Tests calcFlopWins exceptions"""
		self.assertRaises(TypeError, lambda: calcFlopWins())

	def testCeiling(self):
		"""Tests if calcFlopWins returns <= 1.0"""
		self.assertTrue(calcFlopWins(2, 3) <= 1.0)

if __name__ == "__main__":
    unittest.main()