# imports
import sys
import os.path

#python -m pip install -U matplotlib
import matplotlib.pyplot as plt
pwlen = 8
lets = len("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")  #testa
#lets = len("abcdefghijklmnopqrstuvwxyzæøåABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ0123456789")
combinations = lets**pwlen

sek = (combinations / 1000000)
mins = sek/60
hours = mins/60
døgn = hours/24

print(f"2 - døgn: {døgn}")

vanligeord = 3000
nums = 10

muligheter = vanligeord*(nums**2)
print(muligheter/1000)