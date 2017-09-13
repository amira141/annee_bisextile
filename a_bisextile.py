#***ANNEE BISEXTILE***

#Déterminer si une année saisie par l'utilisateur est bissextile.

u_a = input("Ecrivez une année pour savoir si celle-ci est bisextile ou non")
A = int(u_a)

if A%4 != 0:
	print("L'année n'est pas bisextile.") 
else: 
	print("L'année est bisextille.")