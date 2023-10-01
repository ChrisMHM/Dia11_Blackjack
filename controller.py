import random


def getRandomCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    cardsListSize = len(cards)
    # print(cardsListSize)
    randomIndex = random.randint(0, cardsListSize - 1)
    # print(f"index: {randomIndex} card: {cards[randomIndex]}")

    return cards[randomIndex]

# for i in range(1000):
#     randomCard = getRandomCard()
#     print(f"The random card selected is {randomCard}")