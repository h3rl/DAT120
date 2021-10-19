# imports
import sys
import os.path

#python -m pip install -U matplotlib
import matplotlib.pyplot as plt

#a)
# Dato og tid;Tid siden start (s);Trykk barometer(bar);Trykk abs(bar);Temperatur

filepath = "trykk_og_temperaturlogg.csv"
absPath = os.path.join(sys.path[0], filepath)
file = open(absPath,"r")
lines = file.readlines()

#fjerne første linje
lines = lines[1:]

dato = []
tid_siden_start = []
trykk_barometer = []
trykk_abs = []
temperatur = []

print(f"len of file {len(lines)}")

for index, line in enumerate(lines, start=1):
  line = line.replace(",",".")
  liste = line.split(";")

  dato.append(liste[0])
  tid_siden_start.append(float(liste[1]))
  if liste[2].isdecimal():
    trykk_barometer.append(float(liste[2]))
  else:
    #må ha dette for at data skal få riktig indeks
    trykk_barometer.append(None)
  trykk_abs.append(float(liste[3]))
  temperatur.append(float(liste[4]))

#b)
plt.subplot(2,2,1)
plt.plot(tid_siden_start,trykk_abs)
plt.ylabel("trykk abs")
plt.xlabel("tid")

plt.subplot(2,2,2)
plt.plot(tid_siden_start,temperatur)
plt.ylabel("temperatur")
plt.xlabel("tid")

#c)
plt.subplot(2,1,2)
plt.hist(temperatur)
plt.ylabel("temperatur")
plt.xlabel("tid")
plt.show()

#d)
for i in range(len(lines)-1):
  tid = tid_siden_start[i]
  nestetid = tid_siden_start[i+1]
  if nestetid - tid != 10:
    print(f"{tid} - {nestetid} = {nestetid - tid}")