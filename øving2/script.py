#imports
import turtle
import math

# #a
# målt_høyde = float(input("Skriv inn høyden: "))

# if målt_høyde >= 120:
#   print("Personen kan ta karusell.")
# else:
#   print("Personen er ikke høy nokk til å ta karusell.")

# #b
# alder = int(input("Skriv inn alder til kunde: "))
# pris = 40

# if alder < 18 or alder >= 67:
#   pris = 20

# print(f"Person {alder}år skal betale {pris}")

# #c
# sum = 0
# while True:
#   tall = int(input("Skriv inn ett positivt tall: "))
#   if tall > 0:
#     sum += tall
#   else:
#     print(f"Den endelige summen er {sum}")
#     break

#d
antall = 0
sum = 0
while True:
  tall = int(input("Skriv inn ett positivt tall: "))
  if tall > 0:
    sum += tall
    antall += 1
  else:
    print(f"Gjennomsnittet av tallene er {sum/antall:.2f}")
    break

# #e

# for i in range(6):
#   turtle.forward(80)
#   turtle.right(60)

# #f

# kanter = int(input("Skriv inn antall kanter:"))
# turtle.speed(1)
# radius = 100
# for kanter in range(3,100):
#   deg = 360/kanter
#   for i in range(kanter):
#     x = math.cos(deg*math.pi/180*i)*radius
#     y = math.sin(deg*math.pi/180*i)*radius
#     turtle.goto(x,y)


#h
antall = int(input("Skriv inn antall ønskede sekskanter:"))
for a in range(antall):
  for i in range(6 + 4):
    turtle.forward(80)
    turtle.right(60)
  turtle.right(120)