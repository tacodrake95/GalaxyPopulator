import random
import sys
import starData
import math

from config import *

class dataBlock:
    def __init__(self, data="", ID=0):
        self.data = data
        self.ID = ID

#<star name="Sol" temp="100" x="0" y="0" size="1.0" numPlanets="0" numGasGiants="0" >


closeStarTag = "\t</star>\n"
closePlanetTag = "\t\t</planet>\n"

def genStarTag(block, name="unnamed-star", temp=100, x=0, y=0, size=1.0, blackHole="false"):
    block.data += starData.starTag % (name, temp, x, y, size, blackHole)
    return block


def genPlanetTag(block, name, rings="false", gasGiant="false", aDens=100, gMul=100, oDist=100, oTheta=0, oPhi=0, rPer=24000, moon=False):
    if moon:
        block.data += starData.moonHeader % (name, block.ID, aDens, gMul, oDist, oTheta, oPhi, rPer)
    else:
        block.data += starData.planetHeader % (name, block.ID, aDens, gMul, oDist, oTheta, oPhi, rPer)
    return block

def genMoon(block, name, moonNum, numMoons, parentSize=0):
    
    ringsChance = random.randint(0,100)
    if ringsChance > 1:
        rings = "false"
    else:
        rings = "true"
    
    aDens = random.randint(0,200)
    gMul = random.uniform(parentSize / 10, parentSize / 2)
    oDist = 200*moonNum/(numMoons+1)
    oTheta = random.randint(0,360)
    oPhi = random.randint(-45,45)

    
    if oPhi < 0:
        oPhi += 180

    rPer = random.randint(1000,100000)
    block = genPlanetTag(block, name, rings, "false", aDens, gMul, oDist, oTheta, oPhi, rPer, True)
    block.data += "\t%s" % closePlanetTag
    block.ID += 1
    return block

def genPlanetSystem(block, name, planetNum, numPlanets, moonNames=[], parentSize=0):
    
    ringsChance = random.randint(0,100)
    if ringsChance > 1:
        rings = "false"
    else:
        rings = "true"
    
    gasGiantChance = random.randint(0,100)
    if (gasGiantChance > (numPlanets - planetNum + 1) * 100):
        gasGiant = "false"
    elif  len(moonNames) >= 2:
        gasGiant = "true"
    else:
        gasGiant = "false"

    aDens = random.randint(0,200)
    if parentSize > 0:
        gMul = random.uniform(parentSize / 10, parentSize / 2)
    else:
        gMul = random.uniform(50,120)
    oDist = random.randint(int(200*planetNum/(numPlanets+1)) -40, int(200*planetNum/(numPlanets+1)))
    oTheta = random.randint(0,360)
    oPhi = random.randint(-45,45)

    
    if oPhi < 0:
        oPhi += 180

    rPer = random.randint(1000,100000)
    
    block = genPlanetTag(block, name, rings, gasGiant, aDens, gMul, oDist, oTheta, oPhi, rPer)
    block.ID += 1

    if len(moonNames) > 0:
        moonNum = 1
        numMoons = len(moonNames)
        for moonName in moonNames:
            block = genMoon(block, moonName, moonNum, numMoons, gMul)
            moonNum += 1
        
    block.data += closePlanetTag
    return block

def genStarSystem(block, name, planetNames):
    
    temp = random.randint(minStarTemp, maxStarTemp)
    
    sDist = random.randint(50, 750)
    sAng = random.uniform(0,2*math.pi)
    x = int(math.cos(sAng) * sDist)
    y = int(math.sin(sAng) * sDist)

    size = random.uniform(minStarSize, maxStarSize)
    numMoons = random.randint(minMoons, maxMoons)

    if random.randint(0,100) > blackHolePct:
        blackHole = "false"
    else:
        blackHole = "true"

    block = genStarTag(block, name, temp, x, y, size, blackHole)

    planetNum = 1
    numPlanets = len(planetNames)
    for name in planetNames:
        moonNames = random.sample(starData.planetNames.split("\n"),numMoons)
        block = genPlanetSystem(block, name, planetNum, numPlanets, moonNames)
        planetNum += 1

    block.data += closeStarTag

    return block



starNameList = random.sample(starData.starNames.split("\n"), numStars)

block = dataBlock(starData.standardHeader + closeStarTag, 3)

numPlanets = random.randint(minPlanets,maxPlanets)

for name in starNameList:
    planetNames = random.sample(starData.planetNames.split("\n"), numPlanets)
    block = genStarSystem(block, name, planetNames)


block.data += "\n</galaxy>"

config = open("planetDefs.xml", "w")

config.write(block.data)
config.close()
