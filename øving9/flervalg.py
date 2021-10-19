# imports
import sys
import os.path

def parseQuestionsFromFile(filepath):
  absPath = os.path.join(sys.path[0], filepath)
  quests = []
  with open(absPath,"r", encoding="ascii") as file:
    lines = file.readlines()
    for line in lines:
      #parse in format <Spørsmålstekst>: <nummeret til korrekt svar> : [<liste med svaralternativer med komma mellom>]
      obj = line.split(":")
      question = obj[0]
      correctAnswerNum = int(obj[1].strip())
      answers = obj[2].strip("").strip("[]").split(",")
      quests.append(Flervalg(question,answers,correctAnswerNum))
  return quests

class Flervalg:
  # Konstruktør
  def __init__(self, question, answers=[], correctAnswerNum=1):
    self.question = question
    self.answers = answers
    self.correctAnswerNum = str(correctAnswerNum)
    self.answeriscorrect = False

  def getCorrectAnswerString(self):
    return self.answers[self.correctAnswerNum-1]

  # Gir en strengrepresentasjon av objektet som skal gi mening for
  # en bruker
  def __str__(self):
    retstr=f"{self.question}\n"
    for idx, spm in enumerate(self.answers):
      retstr+=f"  #{idx+1} - {spm}\n"
    #fjern siste \n
    return retstr[:-1]
  
  def getInput(self):
    ans = input("mitt alternativ: #")
    if ans == self.correctAnswerNum:
      self.answeriscorrect = True
    return

  def getResult(self):
    if self.answeriscorrect:
      print("riktig svar!")
    else:
      print(f"feil, svaret er #{self.correctAnswerNum} {self.getCorrectAnswerString()}")


if __name__ == "__main__":
  oppg = Flervalg("hvor mange hjul har en bil?",["2","4","6"],2)
  oppg2 = Flervalg("hvilken farge er himmelen?",["blå","grønn","lilla","rosa"],1)
  print(oppg)
  oppg.getInput()
  oppg.getResult()
  print(oppg2)
  oppg2.getInput()
  oppg2.getResult()