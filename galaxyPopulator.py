import random
import sys
import starData
import math


#<star name="Sol" temp="100" x="0" y="0" size="1.0" numPlanets="0" numGasGiants="0" >


def genStarTag(name="unnamed-star", temp=100, x=0, y=0, size=1.0, numPlanets=0, numGasGiants=0, blackHole="false"):
    return starData.starTag % (name, temp, x, y, size, numPlanets, numGasGiants, blackHole)

def closeStarTag(starTag=""):
    return "%s\t</star>\n" % starTag

def genPlanetTag(name, dimID, rings="false", gasGiant="false", aDens=100, gMul=100, oDist=100, oTheta=0, oPhi=0, rPer=24000):
    return starData.planetHeader % (name, dimID, aDens, gMul, oDist, oTheta, oPhi, rPer)

def genMoonTag(name, dimID, rings="false", aDens=100, gMul=100, oDist=100, oTheta=0, oPhi=0, rPer=24000):
    return starData.moonHeader % (name, dimID, aDens, gMul, oDist, oTheta, oPhi, rPer)

def closePlanetTag(planetTag):
    return "%s\t\t</planet>\n" % planetTag

try:
    numStars = int(sys.argv[1])
except:
    numStars = 100

try:
    minStarSize = float(sys.argv[2])
except:
    minStarSize = 0.25

try:
    maxStarSize = float(sys.argv[3])
except:
    maxStarSize = 2.5

try:
    minStarTemp = int(sys.argv[4])
except:
    minStarTemp = 50

try:
    maxStarTemp = int(sys.argv[5])
except:
    maxStarTemp = 200

try:
    minPlanets = int(sys.argv[6])
except:
    minPlanets = 2

try:
    maxPlanets = int(sys.argv[7])
except:
    maxPlanets = 5

try:
    minGasGiants = int(sys.argv[8])
except:
    minGasGiants = 0

try:
    maxGasGiants = int(sys.argv[9])
except:
    maxGasGiants = 1

try:
    blackHolePct = int(sys.argv[10])
except:
    blackHolePct = 1

starNameList = random.sample(starData.starNames.split("\n"), numStars)

output = starData.standardHeader

numPlanets = random.randint(2,8)
dimID = 3

for planetNum in range(2, numPlanets+1):
    pName = "Sol %s" % (planetNum)
        
    ringsChance = random.randint(0,100)
    if ringsChance > 1:
        rings = "false"
    else:
        rings = "true"

    gasGiantChance = random.randint(0,100)
    if gasGiantChance > (numPlanets - planetNum + 1) * 100:
        gasGiant = "false"
    else:
        gasGiant = "true"

    aDens = random.randint(0,200)
    gMul = random.randint(50,120)
    oDist = random.randint(int(200*planetNum/numPlanets) -10, int(200*planetNum/numPlanets)+ 10)
    oTheta = random.randint(0,360)
    oPhi = random.randint(-45,45)

    numMoons = random.randint(0,4)

    if oPhi < 0:
        oPhi += 180

    rPer = random.randint(1000,100000)

    output = output + genPlanetTag(pName, dimID, rings, gasGiant, aDens, gMul, oDist, oTheta, oPhi, rPer)
    dimID+=1
    for moonNum in range(1,numMoons+1):
        mName = "%s-%s" % (pName, moonNum)
        
        ringsChance = random.randint(0,100)
        if ringsChance > 1:
            rings = "false"
        else:
            rings = "true"

        gasGiant = "false"
        aDens = random.randint(0,200)
        mgMul = random.randint(int(gMul/5),int(gMul/2))
        oDist = random.randint(int(200*moonNum/numMoons) -10, int(200*moonNum/numMoons)+ 10)
        oTheta = random.randint(0,360)
        oPhi = random.randint(-45,45)

        if oPhi < 0:
            oPhi += 180

        rPer = random.randint(1000,100000)

        output = output + genMoonTag(mName, dimID, rings, aDens, mgMul, oDist, oTheta, oPhi, rPer)
        dimID+=1

    output = closePlanetTag(output)

output = closeStarTag(output)

for name in starNameList:
    temp = random.randint(minStarTemp, maxStarTemp)
    #x = random.randint(-500, 500)
    #y = random.randint(-500, 500)

    sDist = random.randint(50, 500)
    sAng = random.uniform(0,2*math.pi)
    x = int(math.cos(sAng) * sDist)
    y = int(math.sin(sAng) * sDist)

    size = random.uniform(minStarSize, maxStarSize)
    numPlanets = random.randint(minPlanets,maxPlanets)
    numGasGiants = random.randint(minGasGiants,maxGasGiants)
    blackHoleChance = random.randint(0,100)

    if blackHoleChance > blackHolePct:
        blackHole = "false"
    else:
        blackHole = "true"
    
    output = output + genStarTag(name, temp, x, y, size, 0, 0, blackHole)
    
    for planetNum in range(1,numPlanets+1):
        pName = "%s %s" % (name, planetNum)
        
        ringsChance = random.randint(0,100)
        if ringsChance > 1:
            rings = "false"
        else:
            rings = "true"

        gasGiantChance = random.randint(0,100)
        if gasGiantChance > (numPlanets - planetNum + 1) * 100:
            gasGiant = "false"
        else:
            gasGiant = "true"

        aDens = random.randint(0,200)
        gMul = random.randint(50,120)
        oDist = random.randint(int(200*planetNum/numPlanets) -10, int(200*planetNum/numPlanets)+ 10)
        oTheta = random.randint(0,360)
        oPhi = random.randint(-45,45)

        numMoons = random.randint(0,4)

        if oPhi < 0:
            oPhi += 180

        rPer = random.randint(1000,100000)

        output = output + genPlanetTag(pName, dimID, rings, gasGiant, aDens, gMul, oDist, oTheta, oPhi, rPer)
        dimID+=1
        for moonNum in range(1,numMoons+1):
            mName = "%s-%s" % (pName, moonNum)
        
            ringsChance = random.randint(0,100)
            if ringsChance > 1:
                rings = "false"
            else:
                rings = "true"

            gasGiant = "false"
            aDens = random.randint(0,200)
            mgMul = random.randint(int(gMul/5),int(gMul/2))
            oDist = random.randint(int(200*moonNum/numMoons) -10, int(200*moonNum/numMoons)+ 10)
            oTheta = random.randint(0,360)
            oPhi = random.randint(-45,45)

            if oPhi < 0:
                oPhi += 180

            rPer = random.randint(1000,100000)

            output = output + genMoonTag(mName, dimID, rings, aDens, mgMul, oDist, oTheta, oPhi, rPer)
            dimID+=1

        output = closePlanetTag(output)

    output = closeStarTag(output)

output = output + "\n</galaxy>"

config = open("planetDefs.xml", "w")

config.write(output)
config.close()
