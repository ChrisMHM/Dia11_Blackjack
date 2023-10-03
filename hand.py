import cardsController

def getInitialHand():
    """Returns an initial hand to play."""
    initialHand = cardsController.getAHandOfTwoRandomCards()
    return initialHand

def getScore(hand):
    """Returns the sum of the card' scores of a hand."""
    score = 0

    for cardScore in hand:
        score += cardScore

    return score

def getFirstCard(hand):
    firstCardIndex = 0
    return hand[firstCardIndex]

def addANewCard(hand):
    """Adds a new random card to a hand's player and returns the new hand."""
    newCard = cardsController.getRandomCard()
    temporalScore = getScore(hand) + newCard

    if temporalScore <= 21:
        hand.append(newCard)
        return hand
    else:
        acesList = findAces(hand)
        containsAces = len(acesList)

        if containsAces > 0:
            temporalHand = []
            temporalHand = changeAces(hand, acesList)
            print(f"temporal hand: {temporalHand}")
            temporalHand.append(newCard)
            return temporalHand
        else:
            hand.append(newCard)
    return hand

def getHand(hand):
    """Returns the hand list."""
    return hand

def findAces(hand):
    acesIndex = []
    AS = 11

    for index in range(len(hand)):
        if hand[index] == AS:
            acesIndex.append(index)

    return acesIndex

def changeAces(hand, indexes):
    for index in indexes:
        hand[index] = 1

    return hand


# for i in range(50):
#     hand1 = getInitialHand()
#     print(f"******* {i} ********")
#     print(f"hand: {hand1}, score: {getScore(hand1)}")
#     newHand = addANewCard(hand1)
#     print(f"hand: {newHand}, score: {getScore(newHand)}")
