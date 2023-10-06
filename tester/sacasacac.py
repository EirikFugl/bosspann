
navn="eirik"

def siHeiTil(navn):
  print(f"Hei, {navn}!")

siHeiTil(navn)

def arealRektangel(lengde, bredde):
  areal = lengde * bredde
  print(areal)

def arealRektangel2(bredde,lengde):
  areal = lengde * bredde
  print(areal)



print(arealRektangel(4,5))

print(arealRektangel2(5,4))

print(arealRektangel(50,3))


import random as rd

def terning(antallSider):
  """Returnerer et tilfeldig heltall i intervallet [1, antallSider], med begge endepunktente inkludert."""
  return rd.randint(1, antallSider)