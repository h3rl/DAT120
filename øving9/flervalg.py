# imports
import sys
import os.path

class Sporsmaal:
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
    return retstr[:-1]

  def get_svar(self,text):
    while True:
      try:
        answer = int(input(text))
        # hvis vi kommer så langt er svaret et tall
        return answer
      except:
        print("Det du skrev var ikke et tall, prøv igjen")
  
  @property
  def korrekt_svar_tekst(self):
    return f"#{self.correctAnswerIndex}: {self.answers[self.correctAnswerIndex]}"

  def sjekk_svar(self,answer):
    if self.correctAnswerIndex == answer:
      return True
    return False
  #end Sporsmaal

def parseQuestionsFromFile(filepath) -> list[Sporsmaal]:
  try:
    absPath = os.path.join(sys.path[0], filepath)
    quests = []
    with open(absPath,"r",encoding="utf-8") as file:
      lines = file.readlines()
      for line in lines:
        #parse in format <Spørsmålstekst>: <nummeret til korrekt svar> : [<liste med svaralternativer med komma mellom>]
        obj = line.split(":")
        question = obj[0]
        correctAnswerNum = int(obj[1].strip())
        answers = obj[2].replace("[","").replace("]","").replace(" ","").strip().split(",")
        quests.append(Sporsmaal(question,correctAnswerNum,answers))
    return quests
  except:
    print("error parsing file")


if __name__ == "__main__":
  questions = parseQuestionsFromFile("sporsmaalsfil.txt")
  for question in questions:
    print(question)
    spiller1 = question.get_svar("Velg et svaralternativ for spiller 1: ")
    spiller2 = question.get_svar("Velg et svaralternativ for spiller 2: ")
    print("")
    print("Riktig svar: "+question.korrekt_svar_tekst)
    print("")
    print(f"Spiller 1: Riktig") if question.sjekk_svar(spiller1) else print("Spiler 1: Feil")
    print(f"Spiller 2: Riktig") if question.sjekk_svar(spiller2) else print("Spiler 2: Feil")
    print("\n")
  print("Spillet er ferdig.")