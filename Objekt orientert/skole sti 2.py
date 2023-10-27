class Billett():
    def __init__(self):
        self.mva = 0.12
        self.pris = 20

    def beregnPris(self):
        return self.pris + (self.pris * self.mva)
  

class Barnebillett(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.5
  
    def beregnPris(self):
        return super().beregnPris() * self.rabatt
  

class Vernepliktig(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.1

    def beregnPris(self):
        return super().beregnPris() * self.rabatt

class Ukesbillett(Billett):
    def __init__(self):
        super().__init__()
        self.rabatt = 0.8

    def beregnPris(self):
        return super().beregnPris() * 7 * self.rabatt
    

billett = Billett()
barnebillett = Barnebillett()
vernepliktbillett = Vernepliktig()
ukesbillett = Ukesbillett()
print(billett.beregnPris())
print(barnebillett.beregnPris())
print(vernepliktbillett.beregnPris())
print(ukesbillett.beregnPris())