omEirik = {"fornavn": ("Eirik",4),"etternavn": "Midtun","år":2005, "inpot":input()}
print(omEirik)
print(omEirik["fornavn"])
print(omEirik["etternavn"])
print(omEirik["år"])

for noekkel, verdi in omEirik.items():
  print(f"Nøkkel: {noekkel}, verdi: {verdi}.")