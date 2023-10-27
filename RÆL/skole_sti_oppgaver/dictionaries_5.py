dna = "GCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGGTCTGTTCCAAGGGCCTTTGCGTCAGGTGGGCTCAGGATTCCAGGGTGGCTGGACAGC" 
googletranslate = {"A":"U","T":"A","C":"G","G":"C"}
rna=""
for i in dna:
    rna+=googletranslate[i]
print(rna)
kodontabell = {"UUU": "Fenylalanin", "CUU": "Leucin","AUU": "Isoleucin",
               "GUU": "Valin","UUC": "Fenylalanin", "CUC": "Leucin","AUC": "Isoleucin",
               "GUC": "Valin","UUA": "Leucin","CUA": "Leucin","AUA": "Metionin",
               "GUA": "Valin","UUG": "Leucin","CUG": "Leucin","AUG": "Metionin",
               "GUG": "Valin","UCU": "Serin","CCU": "Prolin","ACU": "Treonin",
               "GCU": "Alanin","UCC": "Serin","CCC": "Prolin","ACC": "Treonin",
               "GCC": "Alanin","UCA": "Serin","CCA": "Prolin","ACA": "Treonin",
               "GCA": "Alanin","UCG": "Serin","CCG": "Prolin","ACG": "Treonin",
               "GCG": "Alanin","UAU": "Tyrosin","CAU": "Histidin","AAU": "Asparagin",
               "GAU": "Asparaginsyre","UAC": "Tyrosin","CAC": "Histidin","AAC": "Asparagin",
               "GAC": "Asparaginsyre","UAA": "Stopp","CAA": "Glutamin","AAA": "Lysin",
               "GAA": "Glutaminsyre","UAG": "Stopp","CAG": "Glutamin","AAG": "Lysin",
               "GAG": "Glutaminsyre","UGU": "Cystein","CGU": "Arginin","AGU": "Serin",
               "GGU": "Glycin","UGC": "Cystein","CGC": "Arginin","AGC": "Serin",
               "GGC": "Glycin","UGA": "Stopp","CGA": "Arginin","AGA": "Arginin",
               "GGA": "Glycin","UGG": "Tryptofan","CGG": "Arginin","AGG": "Arginin","GGG": "Glycin"  
               }