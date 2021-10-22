# imports
import sys
import os.path

class Sporsmaal:
  # Konstruktør
  # på formen Sporsmaal("hva er rundt?", 1, ["murstein","ball"])
  def __init__(self, question:str, correctAnswerIndex:int,answers:list[str]) -> None:
    self.question = question
    self.answers = answers
    self.correctAnswerIndex = correctAnswerIndex

  # Gir en strengrepresentasjon av objektet som skal gi mening for
  # en bruker
  def __str__(self) -> str:
    retstr=f"{self.question}\nAlternativer:\n"
    for index, answer in enumerate(self.answers):
      retstr+=f"  #{index}: {answer}\n"
    return retstr[:-1]

  def get_svar(self,text:str) -> int:
    while True:
      try:
        #få svar fra bruker
        answer = int(input(text))

        #hvis vi er kommet hit er svaret et tall.
        # sjekke om det er innenfor svaralternativene
        if answer < 0 or answer >= len(self.answers):
          raise Exception()

        return answer
      except Exception as e:
        #hvis feilen er uten argumenter er det fordi svaret
        #ikke er innenfor alternativene
        if len(e.args) == 0:
          print("Det er ikke et gyldig alternativ, prøv igjen")
        else:
          print("Det du skrev var ikke et tall, prøv igjen")
  
  #gir riktig svar som alternativ nr og alternativ
  @property
  def korrekt_svar_tekst(self) -> str:
    return f"#{self.correctAnswerIndex}: {self.answers[self.correctAnswerIndex]}"

  #sjekker om gitt svar er riktig eller feil
  def sjekk_svar(self,answeridx:int) -> bool:
    if self.correctAnswerIndex == answeridx:
      return True
    return False
  
  #enhetstest for modulen Sporsmaal
  def _enhetstest(self):
    return False
  #end Sporsmaal

#leser spørsmålene fra en fil.
def parseQuestionsFromFile(filepath) -> list[Sporsmaal]:
  try:
    #få den absolutte pathen til fila
    absPath = os.path.join(sys.path[0], filepath)
    quests = []
    #åpne fila
    with open(absPath,"r",encoding="utf-8") as file:
      #lese linjer til liste
      lines = file.readlines()
      #itterere linjene
      for line in lines:
        #parse in format <Spørsmålstekst>: <nummeret til korrekt svar> : [<liste med svaralternativer med komma mellom>]
        obj = line.split(":")
        question = obj[0]
        correctAnswerNum = int(obj[1].strip())
        # fjerne brackets og mellomrom, deretter splitte ved ",".
        answers = obj[2].replace("[","").replace("]","").replace(" ","").strip().split(",")
        # lage et spørsmål med samlet data
        quests.append(Sporsmaal(question,correctAnswerNum,answers))
    
    #returnerer alle lagde spørsmål
    return quests
  except:
    #en feil oppsto
    print("feil ved lesing av fil")

class Spiller:
  def __init__(self,navn:str) -> None:
    self.navn = navn
    self.valgt = 0
    self.poengsum = 0

#funksjonen lager en liste med spilere der navnet blir gitt av bruker.
def lagSpillere() -> list[Spiller]:
  liste = []
  try:
    print("Skriv inn navn på spillerne. Avslutt med tom linje.")
    while True:
      spillernr = len(liste)+1
      navn = str(input(f"Navnet til spiller {spillernr}: "))
      if navn =="":
        break
      liste.append(Spiller(navn))
  except:
    print("Ukjent feil")

  return liste

if __name__ == "__main__":
  questions = parseQuestionsFromFile("sporsmaalsfil.txt")
  spillere = lagSpillere()
  for question in questions:
    print(question)
    for spiller in spillere:
      spiller.valgt = question.get_svar(f"Velg et svaralternativ for spiller {spiller.navn}: ")
    
    print("")
    print("Riktig svar var: "+question.korrekt_svar_tekst)

    for spiller in spillere:
      if question.sjekk_svar(spiller.valgt):
        print(f"{spiller.navn}: Riktig")
        spiller.poengsum += 1
      else:
        print(f"{spiller.navn}: Feil")
    print("")
  print("Spillet er ferdig. her er resultatene")

  spillere.sort(key=lambda spiller:spiller.poengsum,reverse=True)
  for index, spiller in enumerate(spillere):
    print(f"#{index+1} - {spiller.navn} {spiller.poengsum}")
