import unittest
from translator import englishToFrench, frenchToEnglish

class TestEtf(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Yes'), 'Oui')
        self.assertNotEqual(englishToFrench('Yes'), 'Non')

class TestFte(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertNotEqual(frenchToEnglish('Non'), 'Yes')
        
if __name__ == '__main__':
    unittest.main()
