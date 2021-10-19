#imports
import math

#a)
def bussbillett(alder):
  pris = 40
  if alder < 18 or alder >= 67:
    pris = 20
  return pris

#b)
alder = int(input("Skriv inn alder til kunde: "))
pris = bussbillett(alder)
print(f"Person {alder} år skal betale {pris}")

#c)
alder = int(input("Skriv inn alder til kunde: "))
if alder <= 0:
  print("Alderen må være mer en 0")
else:
  pris = bussbillett(alder)
  print(f"Person {alder}år skal betale {pris}")

#d)
def regn_kinetiskenergi(m,v):
  ke = .5 * m * math.pow(v,2)
  return ke

#e)
masse = int(input("Skriv inn masse til objektet: "))
fart = int(input("Skriv inn fart til objektet: "))
kinetiskenergi = regn_kinetiskenergi(masse,fart)
print(f"Objektet med farten {fart} og massen {masse} har ke={kinetiskenergi:.2f}")

#f)
def euclidske_avstand(px,py):
  return math.sqrt(math.pow(px,2) + math.pow(py,2))

#g)
def avstand_mellom_to_punkter(x1,y1,x2,y2):
  delta_x = x2 - x1
  delta_y = y2 - y1
  avstand = euclidske_avstand(delta_x,delta_y)
  return avstand

#h
p1 = str(input("Skriv inn punkt 1 på formen x,y: "))
p2 = str(input("Skriv inn punkt 2 på formen x,y: "))

p1a = [float(pnt) for pnt in p1.split(",")]
p2a = [float(pnt) for pnt in p2.split(",")]

p1x, p1y = p1a
p2x, p2y = p2a

avstand = avstand_mellom_to_punkter(p1x,p1y,p2x,p2y)
print(f"Avstanden mellom ({p1x},{p1y}) og ({p2x},{p2y}) er {avstand:.2f}")

