import cardsController

deck = cardsController.cards
initialHand = cardsController.getAHandOfTwoRandomCards(deck)
newHand = []

def addANewCard(actualHand, deck):
    """Adds a new random card to a hand of a player."""
    print(actualHand)
    newCard = cardsController.getRandomCard(deck)
    print(newCard)
    actualHand.append(newCard)

    return actualHand

def getHand(actualHand):
    return actualHand

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

# newHand = addANewCard(initialHand, deck)
# print(newHand)