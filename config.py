import math

minDIMID = 3
numArms = 3
numGalaxies = 2
incPerCyc = 0.5
spirSeverity = 1
numSystems = 200
minStars = 0
maxStars = 1
minStarSize = 0.25
maxStarSize = 2.5
minStarTemp = 50
maxStarTemp = 200
minStarDist = 5
maxStarDist = 1000
minPlanets = 2
maxPlanets = 5
minPlanetG = 50
maxPlanetG = 150
minPlanetAtm = 10
maxPlanetAtm = 200
maxPlanetDistance = 200
minPlanetTheta = 0
maxPlanetTheta = 360
minPlanetRotPer = 1000
maxPlanetRotPer = 100000
minPlanetSea = 32
maxPlanetSea = 96
minMoons = 1
maxMoons = 3
minMoonAtm = 0
maxMoonAtm = 100
minMoonTheta = 0
maxMoonTheta = 360
minMoonRotPer = 1000
maxMoonRotPer = 100000
minMoonSea = 32
maxMoonSea = 96
blackHolePct = 1
ringsPct = 1
solDist = .25
#starSpread = 2
rescaleFactor = 1
starSpread = (maxStarDist * rescaleFactor) / (numSystems * incPerCyc)

with open('stars.txt', 'r') as starFile:
    starNames = starFile.read()


starList = starNames.split("\n")

# From https://www.fantasynamegenerators.com/planet_names.php and https://github.com/sayamqazi/planet-name-generator
with open('planets.txt', 'r') as planetFile:
    planetNames = planetFile.read()

planetList = planetNames.split("\n")