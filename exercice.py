#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici


# TODO: Définissez vos fonction ici

# Version du prof:
def exercice1(file1, file2):
    with open(file1, encoding="utf-8") as f1, open(file2, encoding="utf-8") as f2:
        for index, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"les fichiers sont differents sur la ligne {index + 1}")
                break

def exercice2(file1, new_file):
    with open(file1, encoding="utf-8") as f1, open(new_file, 'w', encoding="utf-8") as nf:
        for line in f1:
            for i in line:
                nf.write(i)
                if i == " ":
                    nf.write("   ")

"""
version du prof:

def exercice2(file1, new_file):
    with open(file1, encoding="utf-8") as f1, open(new_file, 'w', encoding="utf-8") as nf:
        for line in f1:
            words = line.split()
            triple_line = "   ".join(words)
            nf.write(triple_line)

"""



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    exercice1(r"C:\Users\Homer\Documents\GitHub\c04-ch8-exercices-homer-crypto\exemple.txt",
              r"C:\Users\Homer\Documents\GitHub\c04-ch8-exercices-homer-crypto\exemple2")

    exercice2(r"C:\Users\Homer\Documents\GitHub\c04-ch8-exercices-homer-crypto\exemple.txt", "nouveau_fichier.txt")