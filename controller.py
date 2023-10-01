import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def getRandomCard(deck):
    """Return a random card from a deck of any size."""
    cardsListSize = len(deck)
    # print(cardsListSize)
    randomIndex = random.randint(0, cardsListSize - 1)
    # print(f"index: {randomIndex} card: {cards[randomIndex]}")

    return cards[randomIndex]

# for i in range(1000):
#     randomCard = getRandomCard()
#     print(f"The random card selected is {randomCard}")

def getAHandOfTwoRandomCards(deck):
    """Returns a hand of two random cards from a deck."""
    randomCardsList = []
    for i in range(2):
        randomCard = getRandomCard(deck)
        randomCardsList.append(randomCard)

    return randomCardsList



# print(f"player cards: {playerCards}, dealer cards {dealerCards}")

def sumOfAHand(hand):
    """Returns the sum of the card values of a hand."""
    sum = 0

    for cardValue in hand:
        sum += cardValue

    return sum

# for i in range(100):
#     playerHand = getAHandOfTwoRandomCards(cards)
#     dealerHand = getAHandOfTwoRandomCards(cards)
#     sumOfPlayerHand = sumOfAHand(playerHand)
#     sumOfDealerHand = sumOfAHand(dealerHand)

#     print(f"player's hand: {playerHand}, sum {sumOfPlayerHand}")
    # print(f"dealer's hand: {dealerHand}, sum {sumOfDealerHand}")