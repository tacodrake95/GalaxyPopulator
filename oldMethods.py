class dataBlock:
    def __init__(self, data="", ID=0):
        self.data = data
        self.ID = ID
        self.pSize = 0

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

