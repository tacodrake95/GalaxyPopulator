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

# taken from https://stackoverflow.com/questions/783897/truncating-floats-in-python
def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

# generate a star tag, append it to the block, and return the block
def genStarTag(block, name="unnamed-star", temp=100, x=0, y=0, size=1.0, blackHole="false"):
    block.data += starData.starTag % (name, temp, x, y, size, blackHole)
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
    oDist = int(200*planetNum/(numPlanets+1))
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
    oDist = int(200*moonNum/(numMoons+1))
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
    
# generate a star system with planet systems, append it to the block, and return the block
def genStarSystem(block, name, planetNames):
    temp = random.randint(minStarTemp, maxStarTemp)
    
    sDist = random.randint(minStarDist, maxStarDist)
    sAng = random.uniform(0,2*math.pi)
    
    x = int(math.cos(sAng) * sDist)
    y = int(math.sin(sAng) * sDist)

    size = truncate(random.uniform(minStarSize, maxStarSize), 1)
    
    
    if random.randint(0,100) > blackHolePct:
        blackHole = "false"
    else:
        blackHole = "true"

    block = genStarTag(block, name, temp, x, y, size, blackHole)

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
starNameList = random.sample(starData.starNames.split("\n"), numStars)

# initialise block with a standard header
block = dataBlock(starData.standardHeader + closeStarTag, 3)

# generate the stars
for name in starNameList:
    
    # pick number of planets
    numPlanets = random.randint(minPlanets,maxPlanets)
    # grab a sample of planet names
    planetNames = random.sample(starData.planetNames.split("\n"), numPlanets)
    # append data to block
    block = genStarSystem(block, name, planetNames)

# close galaxy tag
block.data += "\n</galaxy>"

output = open("planetDefs.xml", "w")

output.write(block.data)
output.close()
