import unittest

from flervalg import Sporsmaal

sporsmaal = Sporsmaal("Hva er 1+1?",1,["0","2","5"])

class TestSporsmaal(unittest.TestCase):
  def test_sjekk_svar(self):
    sporsmaal.correctAnswerIndex = 1
    self.assertFalse(sporsmaal.sjekk_svar(-10))
    self.assertFalse(sporsmaal.sjekk_svar(0))
    self.assertTrue(sporsmaal.sjekk_svar(1))
    self.assertFalse(sporsmaal.sjekk_svar(2))
    self.assertFalse(sporsmaal.sjekk_svar(3))
    self.assertFalse(sporsmaal.sjekk_svar(300))

  def test_korrekt_svar_tekst(self):
    sporsmaal.correctAnswerIndex = 1
    self.assertIn(sporsmaal.korrekt_svar_tekst,"#1: 2")
    sporsmaal.correctAnswerIndex = 2
    self.assertIn(sporsmaal.korrekt_svar_tekst,"#2: 5")
    

if __name__ == "__main__":
  unittest.main()
