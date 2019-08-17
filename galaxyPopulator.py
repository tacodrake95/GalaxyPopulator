import random
import sys
from starData import starData
from starData import standardHeader




#<star name="Sol" temp="100" x="0" y="0" size="1.0" numPlanets="0" numGasGiants="0" >


def genStarTag(name="unnamed-star", temp=100, x=0, y=0, size=1.0, numPlanets=5, numGasGiants=2, blackHole="false"):
    starTag = '\t<star name="%s" temp="%s" x="%s" y="%s" size="%s" numPlanets="%s" numGasGiants="%s" blackHole="%s">\n\t</star>\n' % (name, temp, x, y, size, numPlanets, numGasGiants, blackHole)
    return starTag

numStars = int(sys.argv[1])
minStarSize = float(sys.argv[2])
maxStarSize = float(sys.argv[3])
minStarTemp = int(sys.argv[4])
maxStarTemp = int(sys.argv[5])
minPlanets = int(sys.argv[6])
maxPlanets = int(sys.argv[7])
minGasGiants = int(sys.argv[8])
maxGasGiants = int(sys.argv[9])
blackHolePct = int(sys.argv[10])

starDataList = starData.split("\n")
starNames = random.sample(starDataList, numStars)

output = standardHeader % (random.randint(minPlanets,maxPlanets), random.randint(minGasGiants,maxGasGiants))



for name in starNames:
    temp = random.randint(minStarTemp, maxStarTemp)
    x = random.randint(-1000, 2500)
    y = random.randint(-1000, 2000)
    size = random.uniform(minStarSize, maxStarSize)
    numPlanets = random.randint(minPlanets,maxPlanets)
    numGasGiants = random.randint(minGasGiants,maxGasGiants)
    blackHoleChance = random.randint(0,100)

    if blackHoleChance > blackHolePct:
        blackHole = "false";
    else:
        blackHole = "true";
    
    output = output + genStarTag(name, temp, x, y, size, numPlanets, numGasGiants, blackHole)

output = output + "\n</galaxy>"

config = open("planetDefs.xml", "w")

config.write(output)
config.close()
