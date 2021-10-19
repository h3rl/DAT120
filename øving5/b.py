#imports
import os.path
import sys

while True:
  try:
    filepath = str(input("Skriv inn navn på fil: "))
    
    # kaster exeption dersom fil ikke eksisterer.
    inn = open(os.path.join(sys.path[0], filepath),"r")

    # Lager fil hvis ikke eksisterer, hvis eksisterer fortsetter den på fila.
    ut = open(os.path.join(sys.path[0], "utfil.txt"),"w")

    eposter = []

    while True:
      rawl = inn.readline()

      # sjekk om vi er eof
      if rawl == "":
        print("eof")
        break
      
      # fjerne mellomrom
      linje = rawl.strip()

      if linje.startswith("From:"):
        # finne start og slutt
        start = linje.find("<") + 1
        slutt = linje.find(">")


        if start >= 0 and slutt >= 0:
          epost = linje[start:slutt]
          eposter.append(epost.lower() + "\n")
    
    # fjerne duplicates
    eposter = list(dict.fromkeys(eposter))

    ut.writelines(eposter)
    break

  except:
    print("filen eksisterer ikke, prøv igjen")
    filnavn = ""

print("ferdig")