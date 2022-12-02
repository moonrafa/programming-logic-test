import unittest
from pergunta3 import hasCombinationSum
class Test(unittest.TestCase):
  def testPergunta3(self):
    self.assertEqual(hasCombinationSum([1, 15, 2, 7, 2, 5, 7, 1, 4], 2), True)
  def test2Pergunta3(self):
    self.assertEqual(hasCombinationSum([1, 15, 2, 7, 2, 5, 7, 1, 4], 1231), False)
  def testNegativeArray(self):
    self.assertEqual(hasCombinationSum([-1, 21, -89, -7], 14), True)
  def testNegativeSum(self):
    self.assertEqual(hasCombinationSum([-10, 45, 2, -7], -17), True)
  def testZeroSum(self):
    self.assertEqual(hasCombinationSum([1, 21, -89, -1], 0), True)


    
if __name__ == '__main__':
  unittest.main()
