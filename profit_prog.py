from def_float_obli import *

def profit():
#input argent Investi
    inv = def_float_obli("Veuillez entrer le montant investi:")
#input benefice
    pct = def_float_obli("veuillez entrer le pourcentage de benefice:")

#input nombre de mois 
    tem = def_float_obli("veuillez entrer le nombre de mois que vous avez investi:")

#int
    tem =int(tem)
    pct =int(pct)
    inv =int(inv)

    a = inv
    i = 0
#boucle pour le calcul avec les mois
    while tem > i:

        total_b = ((inv/100)*pct)
        inv = inv+total_b
        i = i + 1
    total_bnf = 0
    total_bnf = inv - a

    print ("Ton total de benefice apres "+str(tem)+" mois est de:"+str(total_bnf))
profit()