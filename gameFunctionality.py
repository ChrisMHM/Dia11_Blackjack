import player

FIRST_PLAYER_WINS = 1
SECOND_PLAYER_WINS = 2
NO_WINNER = -1
DRAW = 0

def printPlayersInfo(firstPlayerHand, firstPlayerScore, secondPlayerHand, secondPlayerScore, secondPlayerFirstCard):
    print(f"\tYour cards: {firstPlayerHand}, current score: {firstPlayerScore}")
    print(f"\tDealer cards: {secondPlayerHand}, current score: {secondPlayerScore}")
    print(f"\tComputer's first card: {secondPlayerFirstCard}")

def finalHand(firstPlayerHand, firstPlayerScore, secondPlayerHand, secondPlayerScore):
    print(f"\tYour final hand: {firstPlayerHand}, final score: {firstPlayerScore}")
    print(f"\tComputer's final hand: {secondPlayerHand}, final score: {secondPlayerScore}")

def winner(firstPlayerScore, secondPlayerScore):
    if firstPlayerScore > secondPlayerScore:
        print("You win 😃")
        return FIRST_PLAYER_WINS
    if firstPlayerScore == secondPlayerScore:
        print("Draw 🙃")
        return DRAW
    print("You lose 😤")
    return SECOND_PLAYER_WINS

def blackjack(firstPlayerScore, secondPlayerScore):
    BLACKJACK = 21
    S_BLACKJACK = 22
    if firstPlayerScore == BLACKJACK and secondPlayerScore == BLACKJACK:
        print("Draw 🙃")
        return DRAW
    if firstPlayerScore == BLACKJACK or firstPlayerScore == S_BLACKJACK:
        print("Win with a Blackjack 😎")
        return FIRST_PLAYER_WINS
    if secondPlayerScore == BLACKJACK or secondPlayerScore == S_BLACKJACK:
        print("Lose, opponent has Blackjack 😱")
        return SECOND_PLAYER_WINS
    
    return NO_WINNER
    
def busted(firstPlayerScore, secondPlayerScore):
    if firstPlayerScore > 21:
        print("You went over. You lose 😤")
        return SECOND_PLAYER_WINS
    if secondPlayerScore > 21:
        print("Opponent went over. You win 😁")
        return FIRST_PLAYER_WINS
    return NO_WINNER    

def blackjackOrBusted(firstPlayerScore, secondPlayerScore, newCardsCounter):
    """Return -1 for no winner, 0 for draw, 1 for first player winner and 2 for second player winner."""
    winner = 0

    if newCardsCounter == 0:
        winner = blackjack(firstPlayerScore, secondPlayerScore)
    else:
        winner = busted(firstPlayerScore, secondPlayerScore)

    return winner

def newCard():
    anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")