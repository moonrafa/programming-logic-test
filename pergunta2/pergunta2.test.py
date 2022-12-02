import unittest
from pergunta2 import search

class Test(unittest.TestCase):
  def testPergunta2(self):
    self.assertEqual(search('Goiaba'), 'Maçã -> Morango -> Goiaba')
  def testBiggerPath(self):
    self.assertEqual(search('Cebola'), 'Maçã -> Pera -> Abacaxi -> Laranja -> Cebola')
  def testJustRoot(self):
    self.assertEqual(search('Maçã'), 'Maçã')
  def testNotFound(self):
    self.assertEqual(search('Uva'), 'Item não encontrado')
  def testLetterNotCapitalized(self):
    self.assertEqual(search('abacaxi'), 'Maçã -> Pera -> Abacaxi')
  def testAllCaps(self):
    self.assertEqual(search('PERA'), 'Maçã -> Pera')

    


  

if __name__ == '__main__':
  unittest.main()

