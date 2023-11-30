#
#
#   klasse med karakterer
#   subclass med troll, spiller
#   subclass med level 1, 2, 3, boss for troll
#   level 1, 2, 3 har samme angrep
#
#   Troll:
#   class Troll (hovedegenskaper, har liv, kan angripe, etc.)
#   subclass Troll / TrollKonge (Troll, har visse angrep og visse mengder liv / trollkonge har andre angrep)
#   subclass Troll1,Troll2,Troll3,TrollK (selve multiplier for angrepstyrke / spesialangrep)
#
#
#
#   Spiller:
#   class Spiller (hovedegenskaper)
#   subclass Slv1,Slv2,Slv3 (ulik skade og helse multiplier)


class Ting:
    def __init__(self,navn,helse,mana):
        self.navn = navn
        self.helse = helse
        self.mana = mana
    
    def __str__(self):
        return f"En ting med navn{self.navn} med {self.helse} liv og {self.mana} mana som er i level {self.level}"
        
    def setName(self,nyttNavn):
        self.navn = nyttNavn
    
    def setHelse(self,nyHelse):
        self.helse = nyHelse
    
    def setLevel(self,nyttLevel):
        self.level = nyttLevel

    def bliTruffet(self,skade):
        self.helse -= skade
        if self.helse <= 0:
            self.helse=0
    
    def atk1(self):
        



class Troll(Ting):
    def __init__(self):
        super().__init__()

