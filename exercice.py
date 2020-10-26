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



if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    comparerDeuxFichiers('./exemple.txt', './exemple_2.txt')
    exercice2('./exemple.txt', './exemple_2.txt')

    pass
