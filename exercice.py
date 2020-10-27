#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici




# TODO: Définissez vos fonction ici
def comparerDeuxFichiers(nomFichierUn, nomFichierDeux):
    with open(nomFichierUn, encoding='utf-8') as fichierUn, open(nomFichierDeux, encoding='utf-8') as fichierDeux:
        for index, ligneFUn in enumerate(fichierUn):
            ligneFDeux = fichierDeux.readline()

            if ligneFUn != ligneFDeux:
                print(f"Les fihciers sont différents! À la ligne {index + 1}, on a :")
                print(ligneFUn)
                print("et on a :")
                print(ligneFDeux)
                break

def exercice2(nomFichierUn, nomFichierDeux):
    with open(nomFichierUn, encoding='utf-8') as fichierDepart, open(nomFichierDeux, "w", encoding='utf-8') as fichierArrivee:
        for ligne in fichierDepart:
            nouvLigne = ligne.replace(" ", '   ')
            fichierArrivee.write(nouvLigne)

def exercice3(nomFichierUn, nomFichierDeux):
    with open(nomFichierUn, encoding='utf-8') as fichierNotes, open(nomFichierDeux, "w", encoding='utf-8') as fichierResultats:
        les_notes = fichierNotes.readlines()
        for note in les_notes:
            calcul = int(note) // 5
            calcul = calcul * 5

            if calcul < PERCENTAGE_TO_LETTER["F"][0]:
                fichierResultats.write(str(note.strip("\n")) + " " + str(PERCENTAGE_TO_LETTER["F"][0]) + "\n")
                break

            for lettre, valeur in PERCENTAGE_TO_LETTER.items():
                if valeur[0] <= calcul:
                    fichierResultats.write(str(note.strip("\n")) + " " + lettre + "\n")
                    break



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    comparerDeuxFichiers('./exemple.txt', './exemple_2.txt')
    exercice2('./exemple.txt', './exemple_2.txt')
    exercice3('./notes.txt', './lettres.txt')
    pass
