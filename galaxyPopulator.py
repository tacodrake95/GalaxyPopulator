import random
import sys
import starData
import math

from config import *

def truncate(f):
    sF = str(f).split(".")
    intComp = sF[0]
    decComp = sF[1][0]
    return float(intComp + "." + decComp)

class tag:
    def __init__(self, name="", prop=[], vals=[]):
        self.name = name
        self.prop = [prop, vals]

    def toXML(self):
        out = "<%s" % self.name
        for i in range(0,len(self.prop[0])):
            data = self.prop[1][i]

            if type(data) == float:
                data = truncate(data)

            out = '%s %s="%s"' % (out, self.prop[0][i], data)

        vLen = len(self.prop[0])
        dLen = len(self.prop[1])
        if vLen < dLen:
            for i in range(dLen-vLen, dLen):
                out = "%s %s" % (out, self.prop[1][i])

        return "%s>" % out

class dataBlock:
    def __init__(self, 
                 name="NAME",
                 data=[],
                 prop=[],
                 vals=[]):

        self.data = [tag("%s" % name, prop, vals),
                     data,
                     tag("/%s" % name)]

    def append(self, data):
        self.data[1].append(data)
        
    def toXML(self):
        header = self.data[0].toXML()
        data = self.data[1]
        footer = self.data[2].toXML()
        dType = type(data)
        if dType==list:
            out = ""
            for i in range(len(data)):
                dType = type(data[i])
                if dType == dataBlock:
                    out = "%s%s\n" % (out, data[i].toXML())
                else:
                    out = "%s%s\n" % (out, data[i])
            return "%s\n%s%s" % (header, out, footer)
        elif dType == dataBlock:
            return "%s\n%s\n%s" % (header, data.toXML(), footer)
        else:
            return "%s%s%s" % (header, data, footer)

class planet:
    def __init__(self, 
                 name="untitled-planet", 
                 dimID=0, 
                 distance=1, 
                 pSize=200, 
                 aDens=random.randint(minPlanetAtm,maxPlanetAtm), 
                 oTheta = random.randint(minPlanetTheta,maxPlanetTheta),
                 oPhi = random.randint(-45,45)%360,
                 rPer = random.randint(minPlanetRotPer,maxPlanetRotPer),
                 seaLevel = random.randint(minMoonSea,maxMoonSea)):

        if random.randint(0,100) > ringsPct:
            rings = "false"
        else:
            rings = "true"

        prop=["name", "DIMID"]
        vals=[name, dimID]

        gMul = random.randint(int(pSize / 4), int(pSize/ 2))
        oDist = int(maxPlanetDistance * distance)
        
        data = [dataBlock("isKnown", "false"),
                dataBlock("atmosphereDensity", aDens),
                dataBlock("gravitationalMultiplier", gMul),
                dataBlock("orbitalDistance", oDist),
                dataBlock("orbitalTheta", oTheta),
                dataBlock("orbitalPhi", oPhi),
                dataBlock("rotationalPeriod", rPer),
                dataBlock("seaLevel", seaLevel)]
        self.data = dataBlock("planet", data, prop, vals)

    def genMoons(self, num, startID):
        print("generating %s moons for %s" % (num, self.data.data[0].name))
        for i in range(num):
            name = random.choice(starData.planetList)
            self.data.append(planet(name, startID+i, i/num, self.data.data[1][2].data[1]).data)
        return self

class star:
    def __init__(self,
                 name="unnamed-star",
                 sDist=random.randint(minStarDist, maxStarDist),
                 sAng=random.uniform(0,2*math.pi),
                 blackHole="false"):

        temp = random.randint(minStarTemp, maxStarTemp)
        
        x = int(math.cos(sAng) * sDist * starSpread)
        y = int(math.sin(sAng) * sDist * starSpread)

        size = truncate(random.uniform(minStarSize, maxStarSize))
    
    
        if random.randint(0,1000) <= blackHolePct or blackHole == "true":
            blackHole = "true"
        else:
            blackHole = "false"

        prop=["name", 
              "temp", 
              "x", 
              "y", 
              "size", 
              "numPlanets", 
              "numGasGiants", 
              "blackHole"]

        vals=[name,
              temp,
              x,
              y,
              size,
              0,
              0,
              blackHole]

        self.data = dataBlock("star", [], prop, vals)

    def genPlanets(self, num, dimID):
        for i in range(num):
            name = random.choice(starData.planetList)
            numMoons=random.randint(minMoons, maxMoons)
            distance=i/num
            pSize=200
            self.data.append( planet( name, dimID, distance ).genMoons( numMoons, dimID+1 ).data )
            dimID+=numMoons+1
        return dimID


galaxy=dataBlock("galaxy")

starNameList = random.sample(starData.starList, numSystems)
ID = 3
radius = 5
angle = 0

for name in starNameList:
    # pick number of planets
    numPlanets = random.randint(minPlanets,maxPlanets)
    # grab a sample of planet names
    planetNames = random.sample(starData.planetNames.split("\n"), numPlanets)
    # append data to block
    newStar = star(name, radius, angle)
    ID = newStar.genPlanets(random.randint(minPlanets, maxPlanets), ID)
    galaxy.append(newStar.data)
    radius += incPerCyc
    angle +=  (8.64 * spirSeverity / numSystems) + (math.tau / numArms)
  

output = open("planetDefs.xml", "w")
output.write(galaxy.toXML())