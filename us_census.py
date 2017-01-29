# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:08:38 2017

@author: Quentin PC2
"""
from sklearn.linear_model import Perceptron
from sklearn import tree

def chargement(adresse_fichier):
    fichier = open(adresse_fichier, 'r')
    contenu = fichier.readlines()
    fichier.close()
    x = []
    y = []
    for ligne in contenu:
        ligne = ligne.split(', ')
        #on récupère l'age, le code industriel, le code d'occupation, le salaire horaire, le nombre de semaines travaillées par an
        #pour faire au plus simple j'ai choisi des variables ou continues ou dont les classes ont des valeurs entières
        #○il aurait fallu les renormaliser pour éviter que certaines variables prennent le pas sur d'autres.
        interm = []
        for i in [0, 2, 3, 5, 39]:
            interm.append(int(ligne[i]))
        x.append(interm)
        #on met un 1 si on est au dessus de 50 000$
        #pour comparer, on elève les deux derniers caractères qui sont un point et le retour à la ligne
        if ligne[-1][:-2] == '- 50000':
            y.append(0)
        else:
            y.append(1)
    
    return x, y

def comparer(resultat, objectif):
    """
    Affiche le pourcentage de différences entre resultat et objectif
    """
    N_erreurs = 0
    for i in range(len(resultat)):
        if resultat[i] != objectif[i]:
            N_erreurs += 1
    print("Pourcentage de différences :", N_erreurs/len(resultat))
    

def test_perceptron(appr_x, appr_y, test_x = None, test_y = None):
    percept = Perceptron()
    percept.fit(appr_x, appr_y)
    res = percept.predict(appr_x)
#    print(list(zip(res, test_y)))
    print('Perceptron en apprentissage')
    comparer(res, appr_y)
    if test_x and test_y:
        res = percept.predict(test_x)
        print('Arbre en test')
        comparer(res, test_y)

def test_arbre(appr_x, appr_y, test_x = None, test_y = None):
    arbre = tree.DecisionTreeClassifier()
    arbre.fit(appr_x, appr_y)
    res = arbre.predict(appr_x)
    print('Arbre en apprentissage')
    comparer(res, appr_y)
    if test_x and test_y:
        res = arbre.predict(test_x)
        print('Arbre en test')
        comparer(res, test_y)

if __name__ == '__main__':
    appr_x, appr_y = chargement('us_census_full/census_income_learn.csv')
    test_x, test_y = chargement('us_census_full/census_income_test.csv')
    
    test_perceptron(appr_x, appr_y)
    test_arbre(appr_x, appr_y, test_x, test_y)
