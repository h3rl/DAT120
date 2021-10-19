# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 14:35:50 2021

@author: Erlend Tøssebro
"""

# Korttypene som konstanter
KLOVER = 1
RUTER = 2
SPAR = 3
HJERTER = 4

import random

class Kort:
    def __init__(self, korttype, verdi):
        self.korttype = korttype
        self.verdi = verdi
        
    def __str__(self):
        korttypene = ["ingen", "Kløver", "Ruter", "Spar", "Hjerter"]
        if self.verdi == 1:
            return korttypene[self.korttype] + " ess"
        elif self.verdi <= 10:
            return f"{korttypene[self.korttype]} {self.verdi}"
        elif self.verdi == 11:
            return korttypene[self.korttype] + " knekt"
        elif self.verdi == 12:
            return korttypene[self.korttype] + " dame"
        elif self.verdi == 13:
            return korttypene[self.korttype] + " konge"
        else:
            return "Ugyldig kort!"
    

class Kortstokk:
    def __init__(self):
        self.kortene = list()
        
    def lag_kortene(self):
        for t in range(1, 5):
            for v in range(1, 14):
                self.kortene.append(Kort(t, v))
    
    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet
    
    def stokk(self):
       random.shuffle(self.kortene) 

    def __str__(self):
        resultat = f"Kortstokk med {len(self.kortene)} kort\n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat
    

class Spiller:
    def __init__(self, navn, kort):
        self.navn = navn
        self.kort = kort
    

if __name__ == "__main__":
    antall_spillere = int(input("Antall spillere: "))
    spillerne = []
    stokken = Kortstokk()
    stokken.lag_kortene()
    stokken.stokk()
    for i in range(antall_spillere):
        navn = input(f"Navn til spiller {i}:")
        kortet = stokken.trekk()
        print(f"Spilleren {navn} for kortet {kortet}")
        spilleren = Spiller(navn, kortet)
        spillerne.append(spilleren)
    vinnere = list()
    vinnere.append(spillerne[0])
    for spiller in spillerne:
        if spiller == spillerne[0]:
            continue
        if spiller.kort.verdi > vinnere[0].kort.verdi:
            vinnere.clear()
            vinnere.append(spiller)
        elif spiller.kort.verdi == vinnere[0].kort.verdi:
            vinnere.append(spiller)
    print("Vinnere:")
    for spiller in vinnere:
        print(f"{spiller.navn} har {spiller.kort}")
    
