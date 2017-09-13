# -*-coding:Latin-1 -*
#Code pour afficher les accents sur windows

import os #Module qui va importer une fonction pour permettre d'afficher le programme sur windows d'un double clic 

#***ANNEE BISEXTILE*** 

#***************************************

#Une année est bisextile uniquement si :
#elle est un multiple de  4 et pas de 100
#OU 
#elle est un multiple de 400 

#***************************************

#Déterminer si une année saisie par l'utilisateur est bissextile.

u_a = input("Ecrivez une année pour savoir si celle-ci est bisextile ou non"" ") #L'utilisateur rentre une année
try:
	A = int(u_a)
	assert A>0
except ValueError:
	print("Vous n'avez pas saisi un nombre.")
except AssertionError:
	print("L'année saisie est inférieure ou égale à 0.")
#Reste a definir comment ne pas afficher la suite du code si l'année est inférieur ou égale à 0.

if A%400 == 0 or (A%100 != 0 and A%4 == 0) : #Si l'année est un multiple de 4 et pas de 100 ou bien qu'elle est un multiple de 400, elle est bisextile
    print("L'année est bisextile.")

else: #Sinon elle n'est pas bisextile 
    print("L'année nest pas bisextile") 

os.system("pause")