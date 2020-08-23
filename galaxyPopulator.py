import random
import math
import tkinter as tk

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



def genLuna(ID):
    prop=["name", "DIMID"]
    vals=["Luna", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 0),
            dataBlock("gravitationalMultiplier", 17),
            dataBlock("orbitalDistance", 100),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 0),
            dataBlock("rotationalPeriod", 657520),
            dataBlock("seaLevel", 64)]
    return dataBlock("planet", data, prop, vals)

def genVenus(ID):
    prop=["name", "DIMID"]
    vals=["Venus", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 200),
            dataBlock("gravitationalMultiplier", 90),
            dataBlock("orbitalDistance", 30),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 3),
            dataBlock("rotationalPeriod", 480000),
            dataBlock("seaLevel", 64),
            dataBlock("fogColor", "0.9,0.6,0"),
            dataBlock("skyColor", "0.9,0.6,0"),
            dataBlock("biomeIds", "advancedrocketry:hotdryrock"),
            dataBlock("oceanBlock","minecraft:lava")]
    return dataBlock("planet", data, prop, vals)

def genOverworld():
    prop=["name", "DIMID", "dimMapping"]
    vals=["Earth", 0, ""]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 100),
            dataBlock("gravitationalMultiplier", 100),
            dataBlock("orbitalDistance", 45),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 23.5),
            dataBlock("rotationalPeriod", 24000),
            dataBlock("seaLevel", 64)]
    return dataBlock("planet", data, prop, vals)

def genMars(ID):
    prop=["name", "DIMID"]
    vals=["Mars", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 10),
            dataBlock("gravitationalMultiplier", 38),
            dataBlock("orbitalDistance", 65),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 2),
            dataBlock("rotationalPeriod", 24000),
            dataBlock("seaLevel", 64),
            dataBlock("biomeIds", "advancedrocketry:hotdryrock"),            
            dataBlock("fogColor", "0.8,0.2,0"),
            dataBlock("skyColor", "0.8,0.2,0")]
    return dataBlock("planet", data, prop, vals)

def genJupiter():
    prop=["name", "customIcon"]
    vals=["Jupiter", "gasgiantred"]
    data = [dataBlock("gasGiant", "true"),
            dataBlock("atmosphereDensity", 200),
            dataBlock("gravitationalMultiplier", 180),
            dataBlock("orbitalDistance", 100),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 1),
            dataBlock("gas", "hydrogen"),
            dataBlock("gas", "helium")]
    return dataBlock("planet", data, prop, vals)

def genEuropa(ID):
    prop=["name", "DIMID"]
    vals=["Europa", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 0),
            dataBlock("gravitationalMultiplier", 13),
            dataBlock("orbitalDistance", 70),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 2),
            dataBlock("rotationalPeriod", 85000),
            dataBlock("seaLevel", 64),
            dataBlock("biomeIds", "frozen_ocean")]
    return dataBlock("planet", data, prop, vals)

def genSaturn():
    prop=["name", "customIcon"]
    vals=["Saturn", "gasgiantred"]
    data = [dataBlock("gasGiant", "true"),
            dataBlock("atmosphereDensity", 200),
            dataBlock("gravitationalMultiplier", 130),
            dataBlock("orbitalDistance", 140),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 2),
            dataBlock("hasRings", "true"),
            dataBlock("ringColor", "0.8,0.7,0.4"),
            dataBlock("gas", "hydrogen"),
            dataBlock("gas", "helium")]
    return dataBlock("planet", data, prop, vals)

def genEnceladus(ID):
    prop=["name", "DIMID"]
    vals=["Enceladus", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 0),
            dataBlock("gravitationalMultiplier", 11),
            dataBlock("orbitalDistance", 75),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 2),
            dataBlock("rotationalPeriod", 32900),
            dataBlock("biomeIds", "frozen_ocean")]
    return dataBlock("planet", data, prop, vals)

def genTitan(ID):
    prop=["name", "DIMID"]
    vals=["Titan", ID]
    data = [dataBlock("isKnown", "true"),
            dataBlock("atmosphereDensity", 150),
            dataBlock("gravitationalMultiplier", 14),
            dataBlock("orbitalDistance", 175),
            dataBlock("orbitalTheta", 0),
            dataBlock("orbitalPhi", 2),
            dataBlock("rotationalPeriod", 95700),
            dataBlock("seaLevel", 64),
            dataBlock("biomeIds", "advancedrocketry:hotdryrock"),            
            dataBlock("fogColor", "0.8,0.6,0.1"),
            dataBlock("skyColor", "0.8,0.6,0.1")]
    return dataBlock("planet", data, prop, vals)

def genSol(x, y, temp, size):
    Sol = star("Sol",
                 x,
                 y,
                 temp,
                 size,
                 "false")

    Sol.data.append(planet("Mercury",
                      2,
                      0.075,
                      90,
                      200,
                      0,
                      7,
                      240000,
                      16).data)

    Sol.data.append(genVenus(3))
    
    Earth = genOverworld()
    Earth.append(genLuna(4))
    
    Sol.data.append(Earth)
    Sol.data.append(genMars(5))
    Jupiter = genJupiter()
    Jupiter.append(planet("Io",
                          6,
                          0.2,
                          18,
                          0,
                          0,
                          0,
                          42500,
                          65).data)
    Jupiter.append(genEuropa(7))
    Sol.data.append(Jupiter)

    Saturn = genSaturn()
    Saturn.append(genEnceladus(8))
    Saturn.append(genTitan(9))
    Sol.data.append(Saturn)
    return Sol

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
            #print(int(temp/maxStarTemp * len(typeList)))
            cat = typeList[int(temp/maxStarTemp) * len(typeList) - 1]
            name ="%s-%s #%s" % (cat, int(size / maxStarSize * 100), i*nArms + arm)
            if sol:
                newStar = genSol(x + posX, y + posY, temp, size)
            else:
                newStar = star(name, x + posX, y + posY, temp, size)
            nSis = random.randint(minStars, maxStars)

            if nSis > 0:
                newStar.genSisters(name, nSis)
            
            if not sol:
                ID = newStar.genPlanets(random.randint(minPlanets, maxPlanets), ID)
            # append data to block
            
            map.append(newStar.data)
    return ID
    #return map

def distance(tup1, tup2):
    x1 = tup1[0]
    y1 = tup1[1]

    x2 = tup2[0]
    y2 = tup2[1]

    xLen = x2-x1
    yLen = y2-y1

    return math.sqrt(math.pow(xLen, 2) + math.pow(yLen, 2))

def regen():
    


    map=dataBlock("galaxy")
    galaxyNameList = random.sample(bhList, numGalaxies)
    nArms = 4
    ID = genGalaxy(maxSystems, nArms, maxIRad, maxORad, minDIMID, maxSpirSeverity * nArms, map)

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

#output = open("planetDefs.xml", "w")
#output.write(map.toXML())
#output.close()
top = tk.Tk()
top.resizable(0,0)
frame = tk.Frame(top, bg="grey", width=1024, height=768)
frame.pack()
img = tk.PhotoImage(width = 512, height= 512)
#for x in range(512):
#for y in range(512):
        
data = [["black" for x in range(512)] for y in range(512)]



img.put(data, (0,0))
preview = tk.Label(frame, bd=0, image = img)
preview.place(x=512)


sliderVars={"numArms":["Number of arms: ", #Name
                        (2,12), #Min, Max values
                        1,#Steps
                        2],#Default Value
            
            "minDIMID":["Lowest DIMID: ",
                        (3,27),
                        1,
                        3],
            
            "spirSeverity":["Spiral Slope: ",
                            (0,6.28),
                            0.01,
                            1.0],
            
            "numStars":["Number of Stars",
                        (20,3000),
                        10,
                        10],
            
            "iRad":["Inner Radius: ",
                    (1,50),
                    0.1,
                    25],
            
            "oRad":["Outer Radius: ",
                    (50,750),
                    0.1,
                    500],
            "":["",
                (),
                ,
                ]}

sliderLabels=["Number of arms: ","Lowest DIMID: ", "Spiral Slope: ", "Number of Stars: ", "Inner Radius: ", "Outer Radius: "]
sliderValues=[(2,12),(3, 27), (0,6.28),(20,3000), (1,50),(50,750)]
sliderSteps=[1, 1, 0.01, 10, 0.1, 0.1]

variables=[]

nArmsInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Number of Arms: ", from_=2, to=12, resolution=1, variable=numArms)
nArmsInput.place(x=5, y=5)

mDIDInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Lowest DIMID: ", from_=3, to=27, resolution=1, variable=minDIMID)
mDIDInput.place(x=5, y=70)

spirSevInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Spiral Slope: ", from_=0, to=6.28, resolution=0.01, variable=spirSeverity, length=380)
spirSevInput.place(x=120, y=5)

nStarsInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Number of Stars: ", from_=20, to=3000, resolution=10, variable=numStars, length=380)
nStarsInput.place(x=120, y=70)

iRadInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Inner Radius: ", from_=1, to=50, resolution=0.1, variable=iRad, length=495)
iRadInput.place(x=5, y=135)

iRadInput=tk.Scale(frame, orient=tk.HORIZONTAL,bd=0,fg="darkorange",bg="grey", label="Outer Radius: ", from_=50, to=750, resolution=0.1, variable=oRad, length=495)
iRadInput.place(x=5, y=200)

genBut=tk.Button(frame, bd=1, fg="darkorange",bg="grey", text="Regenerate", activeforeground="orange", activebackground="grey")
genBut.place(x=5, y=740)

savBut=tk.Button(frame, bd=1, fg="darkorange",bg="grey", text="Save", activeforeground="orange", activebackground="grey")
savBut.place(x=75, y=740)

top.mainloop()
