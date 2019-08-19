import random
import sys
import starData
import math

from config import *

# class for easily passing data between the various generation functions
class dataBlock:
    def __init__(self, data="", ID=0):
        self.data = data
        self.ID = ID
        self.pSize = 0

# closing tags
closeStarTag = "\t</star>\n"
closePlanetTag = "\t\t</planet>\n"

def truncate(f):
    sF = str(f).split(".")
    intComp = sF[0]
    decComp = sF[1][0]
    return float(intComp + "." + decComp)

# generate a star tag, append it to the block, and return the block
def genStarTag(block, name="unnamed-star", temp=100, x=0, y=0, size=1.0, blackHole="false"):
    block.data += starData.starTag % (name, temp, x, y, size, blackHole)
    block.pSize = size
    return block

def genSubStarTag(block, name = "unnamed-star", temp=100, size=1.0, dist=1.0):
    block.data += starData.starTag2 % (name, temp, size, dist)
    return block

# generate a planet tag, append it to the block, and return the block
def genPlanetTag(block, name, rings="false", gasGiant="false", aDens=100, gMul=100, oDist=100, oTheta=0, oPhi=0, rPer=24000, seaLevel=64, moon=False):
    if moon:
        block.data += starData.moonHeader % (name, block.ID, aDens, gMul, oDist, oTheta, oPhi, rPer, seaLevel)
    else:
        block.data += starData.planetHeader % (name, block.ID, aDens, gMul, oDist, oTheta, oPhi, rPer, seaLevel)
    return block

# generate a planet's data (without the close tag), append it to the block, and return the block
def genPlanet(block, name, planetNum, numPlanets):
    if random.randint(0,100) > ringsPct:
        rings = "false"
    else:
        rings = "true"

    aDens = random.randint(minPlanetAtm,maxPlanetAtm)
    gMul = random.randint(minPlanetG,maxPlanetG)
    oDist = int(maxPlanetDistance*planetNum/(numPlanets+1))
    oTheta = random.randint(minPlanetTheta,maxPlanetTheta)
    oPhi = random.randint(-45,45)
    if oPhi < 0:
        oPhi += 180

    rPer = random.randint(minPlanetRotPer,maxPlanetRotPer)
    seaLevel = random.randint(minPlanetSea,maxPlanetSea)
    
    block = genPlanetTag(block, name, rings, "false", aDens, gMul, oDist, oTheta, oPhi, rPer, seaLevel)
    block.ID += 1
    block.pSize = gMul
    return block

# generate a moon's data (with close tag), append it to the block, and return the block
def genMoon(block, name, moonNum, numMoons):
    if random.randint(0,100) > ringsPct:
        rings = "false"
    else:
        rings = "true"
    
    aDens = random.randint(minMoonAtm,maxMoonAtm)
    gMul = random.randint(int(block.pSize / 10), int(block.pSize/ 2))
    oDist = int(maxPlanetDistance*moonNum/(numMoons+1))
    oTheta = random.randint(minMoonTheta,maxMoonTheta)
    oPhi = random.randint(-45,45)
    if oPhi < 0:
        oPhi += 180

    rPer = random.randint(minMoonRotPer,maxMoonRotPer)
    seaLevel = random.randint(minMoonSea,maxMoonSea)

    block = genPlanetTag(block, name, rings, "false", aDens, gMul, oDist, oTheta, oPhi, rPer, seaLevel, True)
    block.data += "\t%s" % closePlanetTag
    block.ID += 1
    return block

# generate a planet system with moons, append it to the block, and return the block
def genPlanetSystem(block, name, planetNum, numPlanets, moonNames):
    block = genPlanet(block, name, planetNum, numPlanets)

    if len(moonNames) > 0:
        moonNum = 1
        numMoons = len(moonNames)
        for moonName in moonNames:
            block = genMoon(block, moonName, moonNum, numMoons)
            moonNum += 1
        
    block.data += closePlanetTag
    return block
    
def genSupMass(block, name):
    block = genStarTag(block, name, 100, 0, 0, 5.0, "true")
    block.data += closeStarTag
    return block

# generate a star system with planet systems, append it to the block, and return the block
def genStarSystem(block, name, planetNames, sDist=random.randint(minStarDist, maxStarDist), sAng=random.uniform(0,2*math.pi)):
    temp = random.randint(minStarTemp, maxStarTemp)
    
    x = int(math.cos(sAng) * sDist * starSpread)
    y = int(math.sin(sAng) * sDist * starSpread)

    size = truncate(random.uniform(minStarSize, maxStarSize))
    
    
    if random.randint(0,1000) > blackHolePct:
        blackHole = "false"
    else:
        blackHole = "true"

    block = genStarTag(block, name, temp, x, y, size, blackHole)
    numStars = random.randint(minStars, maxStars)
    for i in range(1,numStars):
        temp = random.randint(50,200)
        dist = truncate(((8*i)+random.uniform(-3,3))/numStars)
        size = truncate(random.uniform(block.pSize / 4, block.pSize / 2))
        block = genSubStarTag(block, name, temp, size, dist)

    planetNum = 1
    numPlanets = len(planetNames)

    # generate planets
    for name in planetNames:
        # pick the number of moons for this planet system
        numMoons = random.randint(minMoons, maxMoons)
        # pick moon names
        moonNames = random.sample(starData.planetNames.split("\n"),numMoons)
        # append data to block
        block = genPlanetSystem(block, name, planetNum, numPlanets, moonNames)
        planetNum += 1
    
    block.data += closeStarTag

    return block


# grab a sample of star names
starNameList = random.sample(starData.starNames.split("\n"), numSystems)

# initialise datablock with supermassive black hole
block = dataBlock("",3)
block = genSupMass(block,"Cignus A*")

radius = 50 / starSpread
angle = 0
solCreated=False

print (starSpread)

# generate the stars
for name in starNameList:
    # pick number of planets
    numPlanets = random.randint(minPlanets,maxPlanets)
    # grab a sample of planet names
    planetNames = random.sample(starData.planetNames.split("\n"), numPlanets)
    # append data to block
    if radius >= solDist * maxStarDist and not solCreated:
        # prepend block with a standard header
        solPosX = int(math.cos(angle)*radius)
        solPosY = int(math.sin(angle)*radius)
        solCreated = True
    else:
        block = genStarSystem(block, name, planetNames, radius, angle)
    radius += incPerCyc
    angle += math.pi / (math.pow(math.pi, math.pi) * spirSeverity) + (math.tau / numArms)

# make sure Sol is generated
if not solCreated:
    solPosX = int(math.cos(angle)*maxStarDist)
    solPosY = int(math.sin(angle)*maxStarDist)

block.data = starData.standardHeader % (solPosX, solPosY) + closeStarTag + block.data + "\n</galaxy>"

output = open("planetDefs.xml", "w")

output.write(block.data)
output.close()
