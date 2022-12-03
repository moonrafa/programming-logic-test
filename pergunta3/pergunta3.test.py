import unittest
from pergunta3 import hasCombinationSum
class Test(unittest.TestCase):
  def testPergunta3(self):
    self.assertTrue(hasCombinationSum([1, 15, 2, 7, 2, 5, 7, 1, 4], 2))
  def test2Pergunta3(self):
    self.assertFalse(hasCombinationSum([1, 15, 2, 7, 2, 5, 7, 1, 4], 1231))
  def testNegativeArray(self):
    self.assertTrue(hasCombinationSum([-1, 21, -89, -7], 14))
  def testNegativeSum(self):
    self.assertTrue(hasCombinationSum([-10, 45, 2, -7], -17))
  def testZeroSum(self):
    self.assertTrue(hasCombinationSum([1, 21, -89, -1], 0))


    
if __name__ == '__main__':
  unittest.main()
