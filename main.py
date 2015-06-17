# -*- coding: UTF-8 -*-
import random
from data.distance import *
from data.place import places
from process import ant

timeToVisit = 0
essaisMax = 1000000
essaisRestants = essaisMax
bestAnt = ant.Ant()
arrets = ["Minimum de teleportations","Temps total minimum","Meilleur rapport qualite/prix"]


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
    deltaTime = (bestAnt.durationTravel - currAnt.durationTravel)/currAnt.durationTravel * 100
    deltaLong = (bestAnt.longTravel - currAnt.longTravel)/currAnt.longTravel * 100
    deltaTele = (bestAnt.nbrTeleportation - currAnt.nbrTeleportation)/currAnt.durationTravel * 100

    #si on constate une evolution globale des indicateurs, alors le rapport q/p est meilleur, sinon non
    if (deltaLong+deltaTime+deltaTele) > 0:
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
    essaisRestants -= 1
    anyAnt.generateTravel(timeToVisit)
    print "Fourmi n°" + str(fourmiNbr)

    if (flag is 0 and isFaster(anyAnt)) or (flag is 1 and isShorter(anyAnt)) or (flag is 2 and hasBestValue(anyAnt)):
        bestAnt = anyAnt
        essaisRestants = essaisMax

    #décrémente les hormones
    decrementAll()


print "--------------------------------------------------------"
bestAnt.display()
