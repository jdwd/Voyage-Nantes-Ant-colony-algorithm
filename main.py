# -*- coding: UTF-8 -*-
import random
from data.distance import *
from data.place import places
from process import ant

timeToVisit = 0
essaisMax = 10000 #1000000
essaisRestants = essaisMax
bestAnt = ant.Ant()
arrets = ["Voyage le plus rapide","Voyage le plus court","Voyage avec le meilleur rapport qualite/prix"]


def isFaster(currAnt):
    if bestAnt.durationTravel == 0 or bestAnt.durationTravel > currAnt.durationTravel:
        return True
    else:
        return False

def isShorter(currAnt):
    if bestAnt.longTravel == 0 or bestAnt.longTravel > currAnt.longTravel:
        return True
    else:
        return False

def hasBestValue(currAnt):
    #pourcentage d'évolution
    deltaTime = (float(bestAnt.durationTravel) - float(currAnt.durationTravel))/float(currAnt.durationTravel) * 100.0
    deltaLong = (float(bestAnt.longTravel) - float(currAnt.longTravel))/float(currAnt.longTravel) * 100.0
    deltaTele = (float(bestAnt.nbrTeleportation) - float(currAnt.nbrTeleportation))/float(currAnt.durationTravel) * 100.0


    if(bestAnt.durationTravel == 0 and bestAnt.longTravel == 0):
        return True

    #si on constate une evolution globale des indicateurs, alors le rapport q/p est meilleur, sinon non
    if (deltaLong+deltaTime+deltaTele) > 0.0:
        return True
    else:
        return False

while (timeToVisit < 15 or timeToVisit > 60) :
    try:
        timeToVisit = int(raw_input('Entrez le temps pour chaque visite: '))
    except(ValueError, TypeError) as e:
        pass
#tempsVisite = int(tempsVisite)

flag = -1
while flag < 0 or flag > 2:
    for oneflag in range(len(arrets)):
        print str(oneflag+1) + ": " + arrets[oneflag]
    try:
        flag = int(raw_input('Choisissez votre systeme d\'arret: ')) -1
    except (ValueError, TypeError) as e:
        pass


fourmiNbr = 0
while(essaisRestants > 0):
    anyAnt = ant.Ant()
    fourmiNbr += 1
    print("essais restants:"+str(essaisRestants))
    anyAnt.generateTravel(timeToVisit)
    print "Fourmi n°" + str(fourmiNbr)
    essaisRestants -= 1

    if (flag is 0 and isFaster(anyAnt)) or (flag is 1 and isShorter(anyAnt)) or (flag is 2 and hasBestValue(anyAnt)):
        bestAnt = anyAnt
        essaisRestants = essaisMax
        print("une meilleure fourmi est trouvée !")
        bestAnt.display()

    #décrémente les hormones
    decrementAll()


print "--------------------------------------------------------"
bestAnt.display()
