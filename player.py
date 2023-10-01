import hand

playerInfo = {
    "hand": [],
    "score": 0,
}

def getPlayer():
    """Returns a dictionary with the initial player info."""
    playerInfo["hand"] = hand.getInitialHand()
    playerInfo["score"] = hand.getScore(playerInfo["hand"])

    return playerInfo

def getHand():
    return playerInfo["hand"]

def getScore():
    return playerInfo["score"]

def setHand(newHand):
    playerInfo["hand"] = newHand

def setScore(newScore):
    playerInfo["score"] = newScore

def newHand(actualHand):
    return hand.addANewCard(actualHand)