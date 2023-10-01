import player

def printPlayersInfo(firstPlayerHand, firstPlayerScore, secondPlayerHand, secondPlayerScore, secondPlayerFirstCard):
    print(f"\tYour cards: {firstPlayerHand}, current score: {firstPlayerScore}")
    print(f"\tDealer cards: {secondPlayerHand}, current score: {secondPlayerScore}")
    print(f"\tComputer's first card: {secondPlayerFirstCard}")
    anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
    
    return anotherCard