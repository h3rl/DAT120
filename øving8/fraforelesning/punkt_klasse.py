# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 11:31:01 2021

@author: Erlend Tøssebro
"""

import math

class Punkt:
    # Konstruktør
    def __init__(self, start_x=0, start_y=0):
        self.__x_koordinat = start_x
        self.y_koordinat = start_y

    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_verdi):
        if ny_verdi < 0:
            raise ValueError("Punktet kan ikke ha negativt x-koordinat!")
        self.__x_koordinat = ny_verdi

    # Beregnet egenskap: r
    @property
    def r(self):
        return self.avstand_origo()

    @r.setter
    def r(self, ny_verdi):
        theta = self.theta
        self.x_koordinat = ny_verdi*math.cos(theta)
        self.y_koordinat = ny_verdi*math.sin(theta)

    # Beregnet egenskap: Theta
    @property
    def theta(self):
       return math.acos(self.x_koordinat/self.r)

    @theta.setter
    def theta(self, ny_verdi):
        r = self.r
        self.x_koordinat = r*math.cos(ny_verdi)
        self.y_koordinat = r*math.sin(ny_verdi)

    # Mutator
    def flytt(self, delta_x, delta_y):
        self.x_koordinat += delta_x
        self.y_koordinat += delta_y

    # Query
    def avstand_origo(self):
        return (self.x_koordinat**2 + self.y_koordinat**2)**0.5

    # Avstand mellom to punkter, antar at det som kommer inn er et punkt
    def avstand(self, annet_punkt):
        xdiff = self.x_koordinat - annet_punkt.x_koordinat
        ydiff = self.y_koordinat - annet_punkt.y_koordinat
        return (xdiff**2 + ydiff**2)**0.5

    # Gir en strengrepresentasjon av objektet som skal gi mening for
    # en bruker
    def __str__(self):
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

    # Gir en strengrepresentasjon til mer internt bruk
    def __repr__(self):
        return f"Punkt ({self.x_koordinat}, {self.y_koordinat})"


def avstand_punkter(punkt1, punkt2):
    xdiff = punkt1.x_koordinat - punkt2.x_koordinat
    ydiff = punkt1.y_koordinat - punkt2.y_koordinat
    return (xdiff**2 + ydiff**2)**0.5


def flytt_til_midten(punkt1, punkt2):
    snitt_x = (punkt1.x_koordinat + punkt2.x_koordinat)/2
    snitt_y = (punkt1.y_koordinat + punkt2.y_koordinat)/2
    punkt1.x_koordinat = snitt_x
    punkt1.y_koordinat = snitt_y
    punkt2.x_koordinat = snitt_x
    punkt2.y_koordinat = snitt_y


if __name__ == "__main__":
    punkt1 = Punkt(3, 4)
    print(punkt1)
    print(punkt1.avstand_origo())
    punkt2 = Punkt()
    print(punkt2)
    print(punkt2.avstand_origo())
    punkt1.flytt(2, -1)
    print(punkt1)
    print(punkt1.avstand_origo())
    punkt3 = Punkt(5, 10)
    avstanden = punkt1.avstand(punkt3)
    print(f"Avstanden mellom {punkt1} og {punkt3} er {avstanden}")

    