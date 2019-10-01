import random
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
            for i in range(dLen-1, dLen):
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

class gasGiant:
    def __init__(self,
                 name="untitled-gas-giant",
                 distance=200,
                 oTheta=0,
                 oPhi=0):

        rings = "true"

        if random.randint(0,100) > ringsPct*10:
            rings = "false"

        prop=["name"]
        vals=[name]

        oDist = int(maxGasGiantDistance * distance) + minGasGiantDistance
        
        data =[dataBlock("isKnown", "false"),
               dataBlock("orbitalDistance", distance)]

class planet:
    def __init__(self,
                 name="untitled-planet",
                 dimID=0,
                 distance=1.0, 
                 pSize=200,
                 aDens=100,
                 oTheta = 0,
                 oPhi = 0,
                 rPer = 24000,
                 seaLevel = 64):

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
                dataBlock("seaLevel", seaLevel),
                dataBlock("hasRings", rings)]
        self.data = dataBlock("planet", data, prop, vals)

    def genMoons(self, num, startID):
        for i in range(num):
            name = random.choice(planetList)
            self.data.append(planet(name,
                                    startID+i,
                                    (i+1)/num,
                                    self.data.data[1][2].data[1], 
                                    random.randint(minPlanetAtm,maxPlanetAtm),
                                    random.randint(minPlanetTheta,maxPlanetTheta),
                                    random.randint(-45,45)%360,
                                    random.randint(minPlanetRotPer,maxPlanetRotPer),
                                    random.randint(minMoonSea,maxMoonSea)
                                    ).data)
        return self


class subStar:
    def __init__(self,
                 name="unnamed-star",
                 oDist=1.0,
                 temp=100):
    
        prop=["name", "temp", "separation"]
        vals=[name, temp, oDist, "/"]
        self.data=tag("star", prop, vals)

class star:
    def __init__(self,
                 name="unnamed-star",
                 x=0,
                 y=0,
                 temp = 100,
                 size = 1.0,
                 blackHole="false"):
        
        

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

    def genSisters(self, name="unnamed-sister", num=1):
        for i in range(num):
            subStarData=subStar(name, i+1, random.randint(minStarTemp, maxStarTemp)).data.toXML()
            self.data.append(subStarData)

    def genPlanets(self, num, dimID):
        for i in range(num):
            name = random.choice(planetList)
            numMoons=random.randint(minMoons, maxMoons)
            distance=(i+1)/num

            self.data.append( planet(name, 
                                     dimID,
                                     distance,
                                     200,
                                     random.randint(minPlanetAtm, maxPlanetAtm),
                                     random.randint(minPlanetTheta, maxPlanetTheta),
                                     random.randint(-45, 45)%360,
                                     random.randint(minPlanetRotPer, maxPlanetRotPer),
                                     random.randint(minPlanetSea,maxPlanetSea)).genMoons(numMoons,dimID+1).data)
            dimID+=numMoons+1
        return dimID

def genLuna():
    prop=["name", "DIMID"]
    vals=["Luna", 2]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 0),
            dataBlock("gravitationalMultiplier", 17),
            dataBlock("orbitalDistance", 100),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 0),
            dataBlock("rotationalPeriod", 657520),
            dataBlock("seaLevel", 64)]
    return dataBlock("planet", data, prop, vals)

def genOverworld():
    prop=["name", "DIMID", "dimMapping"]
    vals=["Earth", 0, ""]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 100),
            dataBlock("gravitationalMultiplier", 100),
            dataBlock("orbitalDistance", 100),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 23.5),
            dataBlock("rotationalPeriod", 24000),
            dataBlock("seaLevel", 64)]
    return dataBlock("planet", data, prop, vals)

def lerp(min, max, pos):
    return pos * (max-min) + min

def genGalaxy(nStars, nArms, iRad, oRad, startID, sSev, map, firstRun = True, name = "Sagittarius A*", posX=0, posY=0):
    
    #starNameList = random.sample(starList, nStars)
    
    ID = startID 
    incPerCyc = (oRad - iRad) * nArms / nStars

    supMass = star(name, posX, posY, 0, math.pow(iRad, 1/3), "true")
    map.append(supMass.data)
    angle = random.randint(-180, 180) * math.pi / 180
    for i in range(int(nStars/nArms)):
        # pick number of planets
        numPlanets = random.randint(minPlanets,maxPlanets)
        # grab a sample of planet names
        planetNames = random.sample(planetList, numPlanets)
        radius = (i * incPerCyc) + iRad
        for arm in range(nArms):
            if firstRun and i * nArms + arm == int(solDist * nStars):
                sol = True
            else:
                sol = False
            r = radius + random.uniform(0, oRad * radialJitter)
            a = ((arm / nArms) + sSev / ((i+1) * math.pow(nArms, 2)) + random.uniform(-angularJitter/2, angularJitter/2)) * (math.pi * 2)

            maj = r + skew / r
            min = r - skew / r

            x = int(math.cos(a * skew + angle) * maj)
            y = int(math.sin(a / skew + angle) * min)

            temp = int(lerp(minStarTemp, maxStarTemp, i * nArms / nStars)) + random.randint(-minStarTemp / 2, maxStarTemp / 2)
            size = truncate(random.uniform(minStarSize, maxStarSize))
            print(int(temp/maxStarTemp * len(typeList)))
            cat = typeList[int(temp/maxStarTemp) * len(typeList) - 1]
            name ="%s-%s #%s" % (cat, int(size / maxStarSize * 100), i*nArms + arm)
            if sol:
                name = "Sol"
            newStar = star(name, x + posX, y + posY, temp, size)
            nSis = random.randint(minStars, maxStars)

            if nSis > 0:
                newStar.genSisters(name, nSis)
            
            if sol:
                luna = genLuna()
                earth = genOverworld()
                earth.append(luna)
                newStar.data.append(earth)
            else:    
                ID = newStar.genPlanets(random.randint(minPlanets, maxPlanets), ID)
            # append data to block
            
            map.append(newStar.data)
    return ID
    #return map

def distance(tup1, tup2):
    print("tup1:")
    print(tup1)
    x1 = tup1[0]
    y1 = tup1[1]

    x2 = tup2[0]
    y2 = tup2[1]

    xLen = x2-x1
    yLen = y2-y1

    return math.sqrt(math.pow(xLen, 2) + math.pow(yLen, 2))


map=dataBlock("galaxy")
galaxyNameList = random.sample(bhList, numGalaxies)

ID = genGalaxy(maxSystems, 4, maxIRad, maxORad, minDIMID, 250, map)

a = random.uniform(-math.pi, math.pi)


r = maxGalR

        
posX = int(math.cos(a) * r)
posY = int(math.sin(a) * r)

ID = genGalaxy(minSystems, 7, minIRad, minORad, ID, minSpirSeverity, map, False, "IC 1101*", posX, posY)

        
"""

galPositions = [(0,0)]

for i in range(numGalaxies):
    print(i)
    numSystems = random.randint(minSystems, maxSystems)
    nArms = random.choice(numArms)
    iRad = random.randint(minIRad, maxIRad)
    oRad = random.randint(minORad, maxORad)
    spirSeverity = random.uniform(minSpirSeverity, maxSpirSeverity)
    
    if i==0:
        first = True
        posX = 0
        posY = 0
    else:
        a = i / (numGalaxies-1) * 2 * math.pi
        r = random.randint(minGalR, maxGalR)
        posX = int(math.cos(a) * r)
        posY = int(math.sin(a) * r)
        first = False

    ID = genGalaxy(numSystems,
                   nArms,
                   iRad,
                   oRad,
                   ID,
                   spirSeverity,
                   map,
                   first,
                   galaxyNameList[i],
                   posX,
                   posY)
"""     

output = open("planetDefs.xml", "w")
output.write(map.toXML())
output.close()