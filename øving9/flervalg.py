# imports
import math

#b)
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