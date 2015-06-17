# -*- coding: UTF-8 -*-
import random
from data.distance import *
from data.place import places
from process import ant


vitesseMax = 5
tempsTeleportation = 5
distanceMax = ((vitesseMax * 1000) / 60) * 5
timeToVisit = 0
essaisMax = 1000000
essaisRestants = essaisMax

meilleurNombreTeleportations = -1
meilleureDistance = 0
meilleurTemps = -1
meilleurChemin = []

arrets = ["Minimum de teleportations","Temps total minimum","Meilleur rapport qualite/prix"]

def better_teleport(a, b):
    return distances[a][b] > distanceMax

def get_random_point():
    global etapesRealisees
    global places
    choice = -1
    while choice is -1 or choice in etapesRealisees:
        choice = int(random.random() * len(places))
    return choice

def nouvelle_etape(point):
    global tempsTotal
    global timeToVisit
    global etapesRealisees
    etapesRealisees.append(point)
    if len(etapesRealisees) > 0:
        tempsTotal += timeToVisit

def calcul_temps_parcours(a, b):
    global distances
    global vitesseMax
    global tempsTeleportation
    if better_teleport(a, b):
        return tempsTeleportation
    else:
        return distances[a][b] / ((vitesseMax*1000)/60)

def update_high_scores(teleportations, distances, temps):
    global flag
    global meilleurNombreTeleportations
    global meilleurTemps
    if flag is 0:
        if meilleurNombreTeleportations is -1:
            meilleurNombreTeleportations = teleportations
            return True
        elif teleportations < meilleurNombreTeleportations:
                meilleurNombreTeleportations = teleportations
                return True
    elif flag is 1:
        if meilleurTemps is -1:
            meilleurTemps = temps
            return True
        elif temps < meilleurTemps:
                meilleurTemps = temps
                return True

    return False


def envoyer_fourmis(teleportations, distances, temps, chemin):
    global essaisRestants
    global essaisMax
    global meilleurChemin

    # Premier lancement
    if temps is 0:
        return True

    essai = update_high_scores(teleportations, distances, temps)
    if essai:
        essaisRestants = essaisMax
        meilleurChemin = list(chemin)
        return True
    elif essaisRestants <= 0:
        return False
    else:
        essaisRestants -= 1
        return True

"""        """
""" START  """
"""        """


ant1 = ant.Ant()
print("visitedPlaces "+str(ant1.visitedPlaces))
print("CurrPosition "+str(ant1.currPosition))
print("placesStillToVisit "+str(ant1.placesStillToVisit))
i = 0
while len(ant1.placesStillToVisit) != 0:
    i += 1
    print(str(i))
    ant1.goToNextPosition(timeToVisit)
    print("CurrPosition "+str(ant1.currPosition))
    print("visitedPlaces "+str(ant1.visitedPlaces))
    print("placesStillToVisit "+str(ant1.placesStillToVisit))


while (timeToVisit < 15 or timeToVisit > 60) :
    try:
        timeToVisit = int(raw_input('Entrez le temps pour chaque visite: '))
    except(ValueError, TypeError) as e:
        pass
#tempsVisite = int(tempsVisite)

flag = -1
while flag < 0 or flag > 1:
    for oneflag in range(len(arrets)):
        print str(oneflag+1) + ": " + arrets[oneflag]
    try:
        flag = int(raw_input('Choisissez votre systeme d\'arret: ')) -1
    except (ValueError, TypeError) as e:
        pass
    if flag is 2:
        print "Ce systeme n\'est pas encore implémenté !"

tempsTotal = 0
nbrTeleportation = 0
distanceParcourue = 0
etapesRealisees = []

fourmiNbr = 0
while envoyer_fourmis(nbrTeleportation, distanceParcourue, tempsTotal, etapesRealisees):

    etapesRealisees = []
    tempsTotal = 0
    nbrTeleportation = 0
    distanceParcourue = 0

    #startPoint = get_random_point()
    startPoint = 0
    nouvelle_etape(startPoint)

    etapeCourante = startPoint
    stop = False
    while True:
        if len(etapesRealisees) is not len(places):
            prochaine_etape = get_random_point()
        else:
            prochaine_etape = startPoint
            stop = True
        if not better_teleport(etapeCourante, prochaine_etape):
            distanceParcourue += distances[etapeCourante][prochaine_etape]
        else:
            nbrTeleportation += 1

        tempsTotal += calcul_temps_parcours(etapeCourante, prochaine_etape)
        nouvelle_etape(prochaine_etape)
        etapeCourante = prochaine_etape

        if stop:
            break

    #print "Distance parcourue: " + str(distanceParcourue) + " metres"
    #print "Nombre de teleportations: " + str(nbrTeleportation)
    #print "Temps total: " + str(tempsTotal) + " minutes"
    fourmiNbr += 1
    print "Fourmi n°" + str(fourmiNbr)

print "--------------------------------------------------------"
# print "Plus petite distance parcourue: " + str(meilleureDistance) + " metres"
if flag is 0:
    print "Plus petit nombre de teleportations: " + str(meilleurNombreTeleportations)
elif flag is 1:
    print "Temps le plus court : " + str(meilleurTemps) + " minutes"

print "Meilleur chemin: "
print meilleurChemin
for etape in meilleurChemin:
    print " --> " + str(etape) + ":" + places[etape],
