#***ANNEE BISEXTILE***

#***************************************

#Une année est bisextile uniquement si :
#elle est un multiple de  4 et pas de 100
#OU 
#elle est un multiple de 400 

#***************************************

#Déterminer si une année saisie par l'utilisateur est bissextile.

u_a = input("Ecrivez une année pour savoir si celle-ci est bisextile ou non"" ") #L'utilisateur rentre une année
A = int(u_a)

if A%4 == 0 and A%100 != 0 or A%400 == 0 : #Si l'année est un multiple de 4 et pas de 100 ou bien qu'elle est un multiple de 400, elle est bisextile
    print("L'année est bisextile.")

else: #Sinon elle n'est pas bisextile 
    print("L'année nest pas bisextile") 

