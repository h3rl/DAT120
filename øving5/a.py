while True:
  try:
    målt_høyde = float(input("Skriv inn høyden: "))

    if målt_høyde >= 120:
      print("Personen kan ta karusell.")
    else:
      print("Personen er ikke høy nokk til å ta karusell.")

  except:
    print("Det du skrev inn var ikke en gyldig verdi, prøv igjen")