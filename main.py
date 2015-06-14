# -*- coding: UTF-8 -*-
import random

places = [
    "LE LIEU UNIQUE",
    "NYMPHÉA",
    "DES STATIONS GOURMANDES EN VILLE",
    "AIRE DE JEUX",
    "MUSÉE D'HISTOIRE DE NANTES",
    "PATRICK DOUGHERTY",
    "DE TEMPS EN TEMPS",
    "SANS TITRE",
    "« CANADIENNE »",
    "L'ABSENCE",
    "LA STATION PROUVÉ",
    "LES ANNEAUX",
    "HAB GALERIE",
    "LA CALE 2 CREATEURS",
    "LA GALERIE DES MACHINES ET LE GRAND ÉLÉPHANT",
    "LE CARROUSEL DES MONDES MARINS",
    "L'ARBRE À BASKET",
    "MÉMORIAL DE L'ABOLITION DE L'ESCLAVAGE",
    "MUSÉUM D'HISTOIRE NATURELLE",
    "PARCE QUEUE",
    "THÉÂTRE GRASLIN",
    "LA CIGALE",
    "PASSAGE POMMERAYE",
    "LE NID",
    "SUSPENS DE NANTES, 2012",
    "TOMBEAU DE FRANÇOIS II",
    "PORTE SAINT-PIERRE",
    "CHAPELLE DE L’ORATOIRE",
    "JARDIN DES PLANTES"
]

distances = [
    [0, 97, 165, 260, 259, 303, 1330, 1450, 1370, 1270, 1970, 2340, 2640, 2120, 1750, 1960, 1840, 1600, 1470, 1470, 1260, 1270, 1100, 980, 642, 476, 540, 481, 439],
    [97, 0, 81, 262, 199, 246, 1230, 1480, 1400, 1300, 2010, 2360, 2670, 2130, 1780, 1970, 1860, 1570, 1450, 1450, 1250, 1260, 1100, 941, 612, 408, 456, 406, 409],
    [165, 81, 0, 204, 126, 165, 1180, 1430, 1360, 1290, 1970, 2340, 2630, 2090, 1750, 194, 1820, 1550, 1390, 1390, 1190, 1190, 1030, 845, 535, 318, 378, 330, 449],
    [260, 262, 204, 0, 120, 121, 1010, 1260, 1170, 1100, 1790, 2140, 2450, 1920, 1560, 1750, 1630, 1370, 1230, 1230, 1030, 1030, 870, 752, 407, 362, 423, 449, 640],
    [259, 199, 126, 120, 0, 50, 1070, 1350, 1270, 1210, 1870, 2240, 2540, 1990, 1660, 1840, 1710, 1460, 1270, 1270, 1070, 1080, 909, 734, 421, 255, 310, 332, 566],
    [303, 246, 165, 121, 50, 0, 1070, 1350, 1270, 1210, 1870, 2240, 2540, 1990, 1660, 1840, 1710, 1460, 1270, 1270, 1070, 1080, 909, 734, 421, 255, 310, 332, 566],
    [1330, 1230, 1180, 1010, 1070, 1070, 0, 396, 342, 534, 835, 1170, 1500, 913, 664, 776, 649, 368, 338, 338, 243, 201, 282, 713, 717, 1140, 1150, 1320, 1640],
    [1450, 1480, 1430, 1260, 1350, 1350, 396, 0, 87, 314, 522, 889, 1180, 693, 288, 409, 358, 344, 622, 622, 631, 605, 685, 1110, 1060, 1470, 1490, 1630, 1890],
    [1370, 1400, 1360, 1170, 1270, 1270, 342, 87, 0, 278, 601, 982, 1260, 757, 380, 583, 487, 372, 593, 593, 572, 534, 616, 1030, 967, 1390, 1410, 1560, 1800],
    [1270, 1300, 1290, 1100, 1210, 1210, 534, 314, 278, 0, 768, 1140, 1390, 962, 530, 790, 719, 640, 844, 844, 771, 735, 768, 1140, 989, 1370, 1390, 1520, 1700],
    [1970, 2010, 1970, 1790, 1870, 1870, 835, 522, 601, 768, 0, 345, 657, 231, 242, 132, 218, 522, 886, 886, 997, 955, 1110, 1540, 1550, 1980, 1990, 2140, 2420],
    [2340, 2360, 2340, 2140, 2240, 2240, 1170, 889, 982, 1140, 345, 0, 345, 263, 606, 390, 502, 812, 1130, 1130, 1280, 1240, 1410, 1820, 1880, 2310, 2320, 2480, 2760],
    [2640, 2670, 2630, 2450, 2540, 2540, 1500, 1180, 1260, 1390, 657, 345, 0, 594, 880, 719, 833, 1130, 1480, 1480, 1620, 1580, 1740, 2160, 2210, 2630, 2640, 2810, 3070],
    [2120, 2130, 2090, 1920, 1990, 1990, 913, 693, 757, 962, 231, 263, 594, 0, 444, 170, 272, 555, 871, 871, 1020, 989, 1150, 1560, 1630, 2060, 2060, 2230, 2550],
    [1750, 1780, 1750, 1560, 1660, 1660, 664, 288, 380, 530, 242, 606, 880, 444, 0, 280, 237, 427, 786, 786, 848, 811, 941, 1370, 1350, 1770, 1780, 1930, 2180],
    [1960, 1970, 194, 1750, 1840, 1840, 776, 409, 583, 790, 132, 390, 719, 170, 280, 0, 120, 432, 781, 781, 901, 871, 1030, 1450, 1500, 1910, 1930, 2080, 2380],
    [1840, 1860, 1820, 1630, 1710, 1710, 649, 358, 487, 719, 218, 502, 833, 272, 237, 120, 0, 301, 667, 667, 785, 752, 905, 1320, 1370, 1790, 1790, 1960, 2260],
    [1600, 1570, 1550, 1370, 1460, 1460, 368, 344, 372, 640, 522, 812, 1130, 555, 427, 432, 301, 0, 374, 374, 493, 455, 613, 1030, 1090, 1520, 1520, 1700, 2020],
    [1470, 1450, 1390, 1230, 1270, 1270, 338, 622, 593, 844, 886, 1130, 1480, 871, 786, 781, 667, 374, 0, 0, 210, 204, 360, 711, 855, 1270, 1270, 1440, 1840],
    [1470, 1450, 1390, 1230, 1270, 1270, 338, 622, 593, 844, 886, 1130, 1480, 871, 786, 781, 667, 374, 0, 0, 210, 204, 360, 711, 855, 1270, 1270, 1440, 1840],
    [1260, 1250, 1190, 1030, 1070, 1070, 243, 631, 572, 771, 997, 1280, 1620, 1020, 848, 901, 785, 493, 210, 210, 0, 43, 157, 542, 666, 1080, 1070, 1260, 1640],
    [1270, 1260, 1190, 1030, 1080, 1080, 201, 605, 534, 735, 955, 1240, 1580, 989, 811, 871, 752, 455, 204, 204, 43, 0, 160, 575, 671, 1090, 1100, 1270, 1650],
    [1100, 1100, 1030, 870, 909, 909, 282, 685, 616, 768, 1110, 1410, 1740, 1150, 941, 1030, 905, 613, 360, 360, 157, 160, 0, 426, 506, 925, 931, 1100, 1490],
    [980, 941, 845, 752, 734, 734, 713, 1110, 1030, 1140, 1540, 1820, 2160, 1560, 1370, 1450, 1320, 1030, 711, 711, 542, 575, 426, 0, 351, 636, 613, 799, 1250],
    [642, 612, 535, 407, 421, 421, 717, 1060, 967, 989, 1550, 1880, 2210, 1630, 1350, 1500, 1370, 1090, 855, 855, 666, 671, 506, 351, 0, 431, 434, 596, 985],
    [476, 408, 318, 362, 255, 255, 1140, 1470, 1390, 1370, 1980, 2310, 2630, 2060, 1770, 1910, 1790, 1520, 1270, 1270, 1080, 1090, 925, 636, 431, 0, 58, 178, 635],
    [540, 456, 378, 423, 310, 310, 1150, 1490, 1410, 1390, 1990, 2320, 2640, 2060, 1780, 1930, 1790, 1520, 1270, 1270, 1070, 1100, 931, 613, 434, 58, 0, 175, 658],
    [481, 406, 330, 449, 332, 332, 1320, 1630, 1560, 1520, 2140, 2480, 2810, 2230, 1930, 2080, 1960, 1700, 1440, 1440, 1260, 1270, 1100, 799, 596, 178, 175, 0, 492],
    [439, 409, 449, 640, 566, 566, 1640, 1890, 1800, 1700, 2420, 2760, 3070, 2550, 2180, 2380, 2260, 2020, 1840, 1840, 1640, 1650, 1490, 1250, 985, 635, 658, 492, 0],
]

vitesseMax = 5
tempsTeleportation = 5
distanceMax = ((vitesseMax * 1000) / 60) * 5
tempsVisite = ""
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
    global tempsVisite
    global etapesRealisees
    etapesRealisees.append(point)
    if len(etapesRealisees) > 0:
        tempsTotal += tempsVisite

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

while not tempsVisite.isdigit():
    tempsVisite = raw_input('Entrez le temps pour chaque visite: ')
tempsVisite = int(tempsVisite)

flag = -1
while flag < 0 or flag > 1:
    for oneflag in range(len(arrets)):
        print str(oneflag+1) + ": " + arrets[oneflag]
    try:
        flag = int(raw_input('Choisissez votre systeme d\'arret: ')) -1
    except (ValueError, TypeError) as e:
        pass
    if flag is 2:
        print "Ce systeme n\'est pas encore implemente !"

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