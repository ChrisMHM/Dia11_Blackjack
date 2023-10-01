import random
import blackjackDeck

CARDS = blackjackDeck.CARDS

def getRandomCard():
    """Return a random card from a deck of any size."""
    deck = CARDS
    cardsListSize = len(deck)
    # print(cardsListSize)
    randomIndex = random.randint(0, cardsListSize - 1)
    # print(f"index: {randomIndex} card: {cards[randomIndex]}")

    return CARDS[randomIndex]

def getAHandOfTwoRandomCards():
    """Returns a hand of two random cards from a deck."""
    deck = CARDS
    randomCardsList = []
    for i in range(2):
        randomCard = getRandomCard()
        randomCardsList.append(randomCard)

    return randomCardsList