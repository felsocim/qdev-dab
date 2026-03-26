import unittest
from dab.account import *

class checkWithdrawalUnitTests(unittest.TestCase):
  def test_authorized(self):
    result = checkWithdrawal(80, 576)
    self.assertTrue(result)
  def test_refusal(self):
    result = checkWithdrawal(160, 90)
    self.assertFalse(result)

if __name__ == '__main__':
  unittest.main()
