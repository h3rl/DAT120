# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:54:03 2021

@author: halva
"""

#2)
# print(3+2*(4+3))

# #3)
# a = 3+2*(4+3)
# print(a*2-9)

# #4)
# val = int(input("Skriv inn et tall: "))
# ch = chr(val)
# print(f"tilsvarende bokstav-verdi for tallet {val} er {ch}")

#5)
# val = input("Skriv inn et tegn: ")
# nr = ord(val)
# print(f"tilsvarende bokstav-verdi for tallet {val} er {nr}")

#6)

# Lese inn et tall fra brukeren, som er antall sekunder objektet har falt.
# b. Regne ut farten i meter pr. sekund etter det antallet sekunder med formelen fart =
# akselerasjon*tid. Akselerasjonen fra tyngdekraften er 9,81 m/s2
# .
# c. Regne ut distansen objektet har falt i meter med formelen distanse = 0,5*fart*tid
# d. Skrive ut fart og distanse.

sekunder = float(input("Skriv in antal sekunder objektet har falt: "))

fart = sekunder * 9.81
distanse = 0.5 * fart * sekunder

print(f"Objektet har falt {distanse:.2f}m og har nå farten {fart:.2f}m/s")