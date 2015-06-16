# -*- coding: UTF-8 -*-
import random
from data.distance import randomPondereNoeud
from data.place import places

__author__ = 'Justine Dewilde'

class Ant:
    def __init__(self):
        firstPosition = int(random.random() * len(places))
        self.visitedPlaces = []
        self.visitedPlaces.append(firstPosition)
        self.initializeStillToVisit(firstPosition)
        self.durationTravel = 0             #tempsTotal
        self.longTravel = 0                 #distanceTotal
        self.currPosition = firstPosition   #point courant
        self.initialPosition = firstPosition #premiere position

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
        if len(self.placesStillToVisit) == 0 :
            newPosition = self.initialPosition
        else :
            #while tru + break equivalent Do-While
            while True:
                newPosition = randomPondereNoeud(self.currPosition)
                if not(newPosition in self.visitedPlaces):
                    break

        return newPosition

    #Fonction permettant de déplacer la fourmi
    def goToNextPosition(self):
        newPosition = self.selectNode()
        self.visitedPlaces.append(newPosition)
        self.placesStillToVisit.remove(newPosition)
        self.currPosition = newPosition


