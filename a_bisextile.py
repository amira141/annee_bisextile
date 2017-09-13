#***ANNEE BISEXTILE***

#Déterminer si une année saisie par l'utilisateur est bissextile.

u_a = input("Ecrivez une année pour savoir si celle-ci est bisextile ou non"" ") #L'utilisateur rentre une année
A = int(u_a)

if A%4 == 0 and A%100 != 0 :  
    print("L'année est bisextile.")
 
elif A%400 == 0: 
    print("L'année est bisextile")

else:
    print("L'année nest pas bisextile") 

