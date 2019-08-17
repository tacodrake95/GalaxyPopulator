import random
from starData import starData
from starData import standardHeader


#<star name="Sol" temp="100" x="0" y="0" size="1.0" numPlanets="0" numGasGiants="0" >

starDataList = starData.split("\n")
starNames = random.sample(starDataList, 200)

def genStarTag(name="unnamed-star", temp=100, x=0, y=0, size=1.0, numPlanets=5, numGasGiants=2, blackHole="false"):
    starTag = '\t<star name="%s" temp="%s" x="%s" y="%s" size="%s" numPlanets="%s" numGasGiants="%s" blackHole="%s">\n\t</star>\n' % (name, temp, x, y, size, numPlanets, numGasGiants, blackHole)
    return starTag

output = standardHeader % (2,1)

for name in starNames:
    temp = random.randint(50, 200)
    x = random.randint(-1000, 2500)
    y = random.randint(-1000, 2000)
    size = random.uniform(0.12, 2.5)
    numPlanets = random.randint(0,2)
    numGasGiants = random.randint(0,1)

    blackHoleChance = random.randint(0,100)

    if blackHoleChance > 1:
        blackHole = "false";
    else:
        blackHole = "true";
    
    output = output + genStarTag(name, temp, x, y, size, numPlanets, numGasGiants, blackHole)

output = output + "\n</galaxy>"

config = open("planetDefs.xml", "w")

config.write(output)
config.close()
