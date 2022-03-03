#Question 2:

import numpy as np
#L'idée est de changer celui qui a choisi pile à chaque tour.
p = 0.7 #probabilité souhaitée d'apparition de pile
J1win = 0 #nombre de victoire de J1
J2win = 0 
n=1000 #nombre de lancers
for lancer in range(n):  
    rand = np.random.rand(1)
    if rand<p and lancer%2==0 or rand>p and lancer%2!=0: #Soit c'est au tour de J1 et il fait pile, soit c'est au tour de J2 et il fait face. 
        J1win+=1
    elif rand<p and lancer%2!=0 or rand>p and lancer%2==0: 
        J2win+=1

if J1win/n > 0.5:
    print(f"J1 gagne, il a gagné {J1win} fois sur {n} parties")
else:
    print(f"J2 gagne, il a gagné {J2win} fois sur {n} parties")
