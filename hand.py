import cardsController

def getInitialHand():
    """Returns an initial hand to play."""
    initialHand = cardsController.getAHandOfTwoRandomCards()
    return initialHand

def addANewCard(hand):
    """Adds a new random card to a hand's player."""
    newCard = cardsController.getRandomCard()
    hand.append(newCard)

    return hand

def getHand(hand):
    """Returns the hand list."""
    return hand

def getScore(hand):
    """Returns the sum of the card' scores of a hand."""
    score = 0

    for cardScore in hand:
        score += cardScore

    return score