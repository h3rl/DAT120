# imports
import math

#b)

class Flervalg:
  # Konstruktør
  
  def __init__(self, question, correctAnswerIndex=1,answers=[]):
    self.question = question
    self.answers = answers
    self.correctAnswerIndex = correctAnswerIndex

  # Gir en strengrepresentasjon av objektet som skal gi mening for
  # en bruker
  def __str__(self):
    retstr=f"{self.question}\nAlternativer:\n"
    for index, answer in enumerate(self.answers):
      retstr+=f"  #{index}: {answer}\n"
    return retstr

  def get_svar(self):
    while True:
      try:
        answer = int(input("Skriv ditt alternativ: "))
        # hvis vi kommer så langt er svaret et tall
        return answer
      except:
        print("Det du skrev var ikke et tall, prøv igjen")
  
  def sjekk_svar(self,answer):
    if self.correctAnswerIndex == answer:
      print("Riktig svar!\n")
      return True
    print(f"Feil, svaret er #{self.correctAnswerIndex}: {self.answers[self.correctAnswerIndex]}\n")
    return False

if __name__ == "__main__":
  oppg = Flervalg("hvor mange hjul har en bil?",1,["2","4","6"])
  oppg2 = Flervalg("hvilken farge er himmelen?",0,["blå","grønn","lilla","rosa"])
  print(oppg)
  inp = oppg.get_svar()
  oppg.sjekk_svar(inp)
  print(oppg2)
  inp = oppg2.get_svar()
  oppg2.sjekk_svar(inp)