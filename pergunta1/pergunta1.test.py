import unittest
from pergunta1 import oneFirst

class Test(unittest.TestCase):

  def testPergunta1(self):
    self.assertEqual(oneFirst([2, 1, 5, 2, 5, 2, 1, 1, 1, 7, 9, 13, 127, 21]), [1, 1, 1, 1, 2, 5, 2, 5, 2, 7, 9, 13, 127, 21])

  def testMostlyOnes(self):
    self.assertEqual(oneFirst([1, 2, 1, 1, 1]), [1, 1, 1, 1, 2])

  def testAllOnes(self):
    self.assertEqual(oneFirst([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1])  
  def testNoOnes(self):
    self.assertEqual(oneFirst([0, 29, 10, 15, 12, 123]), [0, 29, 10, 15, 12, 123])  

    
if __name__ == '__main__':
  unittest.main()
