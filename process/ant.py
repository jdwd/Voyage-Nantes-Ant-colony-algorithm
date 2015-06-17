# -*- coding: UTF-8 -*-
import random
from data.distance import *
from data.place import places

__author__ = 'Justine Dewilde'

class Ant:
    def __init__(self):
        firstPosition = int(random.random() * len(places))
        self.visitedPlaces = []
        self.visitedPlaces.append(firstPosition)
        self.initializeStillToVisit(firstPosition)
        self.durationTravel = 0                 #tempsTotal
        self.nbrTeleportation = 0               #nombre de téléportation <> cout
        self.longTravel = 0                     #distanceTotal
        self.currPosition = firstPosition       #point courant
        self.initialPosition = firstPosition    #premiere position
        self.endTravel = False                  #definit si la fourmi a fini son voyage

    #Fonction permettant d'initialiser la liste des lieux a visiter
    def initializeStillToVisit(self, firstPosition):
        nbrPlaces = len(places)
        i = 0
        self.placesStillToVisit = []

        while(i < nbrPlaces):
            if(i != firstPosition):
                self.placesStillToVisit.append(i)
            i+=1

    #Fonction permettant la selection d'un noeud en fonction des phéromones
    def selectNode(self):
        if len(self.placesStillToVisit) == 0:
            newPosition = self.initialPosition
            self.endTravel = False
        else:
            #while true + break equivalent Do-While
            while True:
                newPosition = randomPondereNoeud(self.currPosition, self.placesStillToVisit)
                if not(newPosition in self.visitedPlaces):
                    break
        return newPosition

    #Fonction permettant de déplacer la fourmi
    def goToNextPosition(self, timeToVisit):

        #selection de la nouvelle position
        newPosition = self.selectNode()

        #actualisation des compteurs
        #temps + prix
        self.durationTravel += timeToVisit

        if isBetterWithTeleportation(self.currPosition, newPosition):
            self.durationTravel += getTeleportationTime()
            self.nbrTeleportation += 1
        else:
            self.durationTravel += getWalkingTime(self.currPosition, newPosition)

        #distance
        self.longTravel += getDistanceToGo(self.currPosition, newPosition)

        #hormones
        incrementHormones(self.currPosition, newPosition)

        #actualisation des variable de positions
        self.currPosition = newPosition
        self.visitedPlaces.append(newPosition)

        if(newPosition == self.initialPosition):
            self.endTravel = True
        else:
            self.placesStillToVisit.remove(newPosition)

    def generateTravel(self, timeToVisit):
        i = 0
        while self.endTravel == False:
            self.goToNextPosition(timeToVisit)

    def display(self):
        print("Fourmi :")
        print("Durée du voyage (mins): "+str(self.durationTravel))
        print("Longueur du voyage (mètres): "+str(self.longTravel))
        print("Nombre de téléportation: "+str(self.nbrTeleportation))
        print("Etapes du voyage:")
        for etape in self.visitedPlaces:
            print("     ->"+places[etape])

