import random
import blackjackDeck

CARDS = blackjackDeck.CARDS

def getRandomCard():
    """Return a random card from a deck of any size."""
    deck = CARDS
    cardsListSize = len(deck)
    randomIndex = random.randint(0, cardsListSize - 1)

    return CARDS[randomIndex]

def getAHandOfTwoRandomCards():
    """Returns a hand of two random cards from a deck."""
    deck = CARDS
    randomCardsList = []
    for i in range(2):
        randomCard = getRandomCard()
        randomCardsList.append(randomCard)

    return randomCardsList