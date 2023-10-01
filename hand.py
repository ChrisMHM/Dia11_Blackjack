import controller

deck = controller.cards
initialHand = controller.getAHandOfTwoRandomCards(deck)
newHand = []

def addANewCard(actualHand, deck):
    print(actualHand)
    newCard = controller.getRandomCard(deck)
    print(newCard)
    actualHand.append(newCard)

    return actualHand



newHand = addANewCard(initialHand, deck)
print(newHand)