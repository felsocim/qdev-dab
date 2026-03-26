import unittest
from dab.account import *

class checkWithdrawalUnitTests(unittest.TestCase):
  def test_authorized(self):
    result = checkWithdrawal(80, 576)
    self.assertTrue(result)

if __name__ == '__main__':
  unittest.main()
