# EditusQuestions

ENONCE :

Il ne vous reste plus qu'une barre de chocolat et vous ne voulez pas la partager avec votre ami.

Il vous propose de jouer à un jeu pour vous départager.

 Vous sortez une pièce de monnaie la dernière qui vous reste et proposez de jouer à "pile ou face"
  
 Votre ami est d'accord, mais il émet un doute quant à la justesse de cette pièce car elle semble a priori asymétrique. 
  
  
  1- Comment pouvez-vous vérifier que la pièce de monnaie est bien juste ou injuste (biaisée) ?
  
  2-  Vous terminez votre vérification et vous vous rendez compte que la pièce est biaisée. Il semblerait que : 
        Les probabilités soient :
                                                                          Pile : 70%
                                                                          Face : 30 %
  vous souhaitez néanmoins jouer à "pile ou face" avec cette pièce. 
  Proposer une approche, une méthodologie pour utiliser cette pièce biaisée afin de vous départager
 
  
  3- Proposer un PoC (Proof-of-Concept) de la question 1 et 2 en utilisant Python ou un langage de votre choix ?

Vous pouvez :
Mentionner les sources (google, pdf, article, etc)
Nous transmettre le POC via github.com (si possible) ou via Readme.txt ( Description de code, ce que fait le code, les versions utilisées etc, comment exécuter le code)
Le code devra être bien documenté .

############# Solutions #############

1- Pour répondre à cette question, on va utiliser la loi des grands nombres qui dit que la moyenne d'un très grand échantillon converge vers l'espérance de notre variable aléatoire. C'est à dire qu'on va lancer un grand nombre de fois la pièce, écrire les résultats à chaque lancer et calculer la moyenne d'apparition de piles (ou de faces).
Cette moyenne ainsi obtenue pourra nous donner une idée de la fiabilité de la pièce, on pourra également donner un intervalle de confiance pour p (probabilité de face ou de pile), pour se faire on va approximer notre loi par la loi Normale centrée réduite grâce au théorème central limite.
Il en ressortira par la suite que:
Iconf = [S/n-1.96*sqrt(var/n),S/n+1.96*sqrt(var/n)] où n = nombre de lancers, S/n = moyenne de l'échantillon et var = variance de l'échantillon, avec un risque alpha = 0.05.

2-Une méthode serait d'inverser sur un grand nombre de lancers la personne qui a sélectionné pile.
C'est à dire, au premier lancer J1 a pile J2 a face, au second lancer J2 a pile et J1 a face. 
Il nous reste ensuite à calculer sur un nombre de lancers pair, celui qui a eu le plus de piles ou de faces au choix.

Une autre approche plus réaliste sur l'instant T (on aimerait éviter de passer trop de temps à lancer plein de pièces sinon le chocolat sera fondu) serait de dire:
On lance une fois la pièce, si c'est pile, on relance, si c'est face le joueur qui a choisi "face" gagne.
Lors du deuxième lancer (s'il a lieu), si c'est pile, le joueur qui a choisi "pile" gagne sinon l'autre gagne.
On se retrouve avec une P("Faire deux fois pile")=0.7*0.7=0.49 vs P("faire au moins une face")=1-P("Faire deux fois pile")=0.51, qui semble être un jeu bien plus équitable que les 0.7/0.3 initiaux.
