class Person:
    """
    Klassen Person
    navn = string

    """
    def __init__ (self, navn, fÅr, kjønn, nasjonalitet):
        """Konstruktør"""
        self.navn = navn
        self.fÅr = fÅr
        self.kjønn = kjønn
        self.nasjonalitet = nasjonalitet
    
    def beregnAlder(self):
        """Beregner alder"""
        alder= 2023-self.fÅr
        return alder
    
    def visInfo(self):
        """Viser info"""
        print(f"Personen er født i {self.fÅr}  og er {self.beregnAlder()} år gammel {self.kjønn} med navnet {self.navn} som kommer fra {self.nasjonalitet}")


eirik = Person("Eirik Midtun", 2005, "mann", "Norge")

eirik.visInfo()


class Elev(Person):
    def __init__(self):
        super().__init__()
        self.årstall = 2023
        self.justeringstall = 15

    def finnTrinn(self):
        vg = super().fÅr()-self.årstall+self.justeringstall
        