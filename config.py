import math

minDIMID = 3 # Starting dimension ID

minIRad = 15 # Minimum inner radius of galactic structures
maxIRad = 25 # Maximum inner radius of galactic structures

minORad = 200 # Minimum outer radius of galactic structures
maxORad = 250 # Maximum outer radius of galactic structures

numArms = [2, 2, 2, 2, 2, 2, 4, 4, 4, 4, 11] # List of numbers of arms to choose from
                              # More instances of the same number increase the likelihood of that type

minSystems = 40 # Minimum number of star systems per galaxy
maxSystems = 50 # Maximum number of star systems per galaxy

minSpirSeverity = 33 # Minimum twist factor
maxSpirSeverity = 37 # Maximum twist factor

minStars = 0 # Minimum number of sister stars
maxStars = 0 # Maximum number of sister stars

numGalaxies = 7 # Number of galactic structures (WIP, not yet implemented)

angularJitter = 0.03125 # How much randomness to apply to angles

radialJitter = 0.03125

minGalR = 500
maxGalR = 1000

minGalSpread = 1000

minStarSize = 0.25 # Smallest star size
maxStarSize = 2.5 # Largest star size

minStarTemp = 50 # Lowest temperature stars
maxStarTemp = 200 # Highest temperature stars

minGasGiantDistance = 120 # Minimum distance from a star to its nearest gas giant
maxGasGiantDistance = 200 # Maximum distance from a star to its furthest gas giant
minPlanets = 1 # Minimum number of planets per system
maxPlanets = 3 # Maximun number of planets per syst
minPlanetG = 50 # Lowest gravity of a given planet
maxPlanetG = 150 # Highest gravity of a given planet
minPlanetAtm = 10 # Minimum planet atmosphere density
maxPlanetAtm = 200 # Maximum planet atmosphere density
maxPlanetDistance = 100 # Maximum distance a planet may be from its parent star
minPlanetTheta = 0 # Lowest allowable planet theta
maxPlanetTheta = 360 # Highest allowable planet theta
minPlanetRotPer = 1000 # Shortest day length
maxPlanetRotPer = 100000 # Longest day length
minPlanetSea = 32 # Lowest sea level on a planet
maxPlanetSea = 96 # Highest sea level on a planet
minMoons = 1 # Minimum moons per planet
maxMoons = 3 # Maximum moons per planet
minMoonAtm = 0 # lowest atmosphere on a moon
maxMoonAtm = 100 # highest atmosphere on a moon
minMoonTheta = 0 # minimum orbital theta of moons
maxMoonTheta = 360 # maximum orbital theta of moons
minMoonRotPer = 1000 # shortest moon day length
maxMoonRotPer = 100000 # longest moon day length
minMoonSea = 32 # lowest moon sea level
maxMoonSea = 96 # highest moon sea level
blackHolePct = 1 # chance a star will be a black hole (Not currently functional)
ringsPct = 1 # chance a given planet / moon will spawn rings
solDist = .25 # distance Sol is from center of main galactic structure
rescaleFactor = 1 # scaling factor for the whole system (applied to all coords)

with open('stars.txt', 'r') as starFile:
    starNames = starFile.read()
    starList = starNames.split("\n")

# From https://www.fantasynamegenerators.com/planet_names.php and https://github.com/sayamqazi/planet-name-generator
with open('planets.txt', 'r') as planetFile:
    planetNames = planetFile.read()
    planetList = planetNames.split("\n")

with open('holes.txt', 'r') as bhFile:
    bhNames = bhFile.read()
    bhList = bhNames.split("\n")