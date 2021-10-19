# imports
from os import kill
import sys
import os.path

# multisplit
import re

#python -m pip install -U matplotlib
import matplotlib.pyplot as plt

#a)
filepath = "oving_1_rein_tekst.txt"
absPath = os.path.join(sys.path[0], filepath)
file = open(absPath,"r",encoding="utf-8")
lines = file.readlines()

data = {}

def replaceall(pattern, replacement, string):
  s = string
  for letter in pattern:
    s = s.replace(letter,replacement)
  return s



for index, line in enumerate(lines):
  line = replaceall(".,\n\t*()"," ",line).lower()
  words = re.split(" ",line)
  for word in words:
    if data.get(word) == None:
      data[word] = []
    if not index + 1 in data.get(word,[]) and word not in {""}:
      data[word].append(index + 1)

for key in sorted(data.keys()):
  ostr = f"{key} - "
  linenrlist = data.get(key,[])
  for linenr in linenrlist:
    ostr += f"{linenr}, "
  #ostr = ostr[:-2]
  print(ostr)