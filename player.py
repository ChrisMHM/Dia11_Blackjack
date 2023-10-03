import hand

def getPlayer():
    """Returns a player dictionary with an initial hand, the score of the hand and the first card value."""
    playerInfo = {
        "hand": [],
        "score": 0,
        "firstCard": 0,
    }

    initialHand = hand.getInitialHand()

    playerInfo["hand"] = initialHand
    playerInfo["score"] = hand.getScore(initialHand)
    playerInfo["firstCard"] = hand.getFirstCard(initialHand)

    return playerInfo

def getHand(playerDict):
    """Returns the actual hand of a player."""
    return playerDict["hand"]

def getScore(playerDict):
    """Returns the actual score of a player."""
    return playerDict["score"]

def getFirstCard(playerDict):
    """Returns the first card of a player's hand."""
    return playerDict["firstCard"]

def setScore(playerDict, newScore):
    """Changes the actual score to a new one."""
    playerDict["score"] = newScore
    return playerDict

def setHand(playerDict, newHand):
    """Changes the actual hand to a new one."""
    playerDict["hand"] = newHand
    return playerDict

def getNewHand(playerDict):
    """Returns a new hand with adding a new card"""
    actualHand = getHand(playerDict)
    newPlayerHand = hand.addANewCard(actualHand)
    playerWithNewHand = setHand(playerDict, newPlayerHand)
    playerHand = getHand(playerWithNewHand)

    return playerHand

def getNewScore(playerDict):
    newHand = getHand(playerDict)
    newPlayerScore = hand.getScore(newHand)
    playerWithNewScore = setScore(playerDict, newPlayerScore)
    playerScore = getScore(playerWithNewScore)

    return playerScore