#Question 1:
import numpy as np

p = 0.7 #probabilité souhaitée d'apparition de pile
n = 1000 #nombre de lancers
alpha = 0.05 #risque
rand = np.random.rand(n) #génération de nombres aléatoires suivant une loi uniforme
piles = np.where(rand<p) #on récupère les indices des nombres de rand tq rand<p
S=len(piles[0]) #Combien de piles ont été faits
mean = S/n #calcul de la moyenne de l'apparition de pile
print(mean)
var=mean*(1-mean)
print(var)
#Ici, c'est inutile car j'ai fixé p, mais on pourrait donner un intervalle de confiance pour p sur un jeu de données réél.
Iconf = [mean-1.96*np.sqrt(var/n),mean+1.96*np.sqrt(var/n)] #Utilisation du théorème central limite.
print(Iconf)
