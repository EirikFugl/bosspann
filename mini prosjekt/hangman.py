# Hangman
import os
import time
from random_word import RandomWords         #importerer moduler jeg trenger

r=RandomWords()
os.system("cls")                            #tømmer terminalen
gjettetOrd="zxzxzxxxzxz"                    #setter gjettetOrd til noe som ikke er i databasen til get_random_word() (hint: linje 27)

print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")

if input("Enter for å starte\t") == "n":
    os.system("cls")
    exit()
os.system("cls")

# # # # # # # # # S T A R T # # # # # # # # # 
tidStart = time.time_ns()

print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")

hemmeligOrd = input("\n\nSkriv inn det hemmelige ordet, eller Enter for tilfeldig")
if hemmeligOrd == "":
    hemmeligOrd=get_random_word()


while hemmeligOrd != gjettetOrd:
    os.system("cls")
    print("#\t#########\t#\n#######  HANGMAN  #######\n#\t#########\t#")

tidSlutt = time.time_ns()

# # # # # # # # # S L U T T # # # # # # # # # 

totTid = round(((tidSlutt-tidStart)/1000000000),4)

print (tidSlutt, tidStart, totTid)