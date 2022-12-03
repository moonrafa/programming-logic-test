import unittest
from pergunta4 import intervalo
class Test(unittest.TestCase):
  def testPergunta4(self):
    self.assertEqual(intervalo([9, 2, 3, 1, 4]), [9, 2, 3, 1, 4, 0, 5, 6, 7, 8])
  def test2(self):    
    self.assertEqual(intervalo([0, 2, 3, 1, 4]), [0, 2, 3, 1, 4])
  def testEmptyArray(self):
    self.assertEqual(intervalo([]), [])
  def testNoMaxNum(self):
    self.assertEqual(intervalo([0, 0, 0]), [0, 0, 0])
  def testNegList(self):
    self.assertEqual(intervalo([-1, 0]), [-1, 0])
    
if __name__ == '__main__':
  unittest.main()