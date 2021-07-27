import csv

entetes = [
     'Colonne1',
     'Colonne2',
     'Colonne3',
     'Colonne4',
     'Colonne5'
]

valeurs = [
     ['Valeur1', 'Valeur2', '', u'Valeur4'],
     ['Valeur6', 'Valeur7', u'Valeur8', u'Valeur9', u'Valeur10'],
     ['Valeur11', 'Valeur12', 'Valeur13', u'Valeur14', u'Valeur15']
]

f = open('monFichier.csv', 'w')
ligneEntete = ",".join(entetes) + "\n"
f.write(ligneEntete)
for valeur in valeurs:
     ligne = ",".join(valeur) + "\n"
     f.write(ligne)

f.close()



