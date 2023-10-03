import player

NO_WINNER = ""
BLACKJACK = 21

def printPlayersInfo(firstPlayerHand, firstPlayerScore, secondPlayerHand, secondPlayerScore, secondPlayerFirstCard):
    """Prints the actual status of player's hands and scores."""
    print(f"\tYour cards: {firstPlayerHand}, current score: {firstPlayerScore}")
    # print(f"\tDealer cards: {secondPlayerHand}, current score: {secondPlayerScore}")
    print(f"\tComputer's first card: {secondPlayerFirstCard}")

def printFinalPlayersInfo(firstPlayer, secondPlayer):
    """Prints the final results after dealer's decisions."""
    firstPlayerHand = player.getHand(firstPlayer)
    secondPlayerHand = player.getHand(secondPlayer)
    firstPlayerScore = player.getScore(firstPlayer)
    secondPlayerScore = player.getScore(secondPlayer)

    print(f"\tYour final hand: {firstPlayerHand}, final score: {firstPlayerScore}")
    print(f"\tComputer's final hand: {secondPlayerHand}, final score: {secondPlayerScore}")

def winner(firstPlayerScore, secondPlayerScore):
    """Returns a string with the winner of two players."""
    isBusted = busted(firstPlayerScore, secondPlayerScore)

    if isBusted == NO_WINNER:
        if firstPlayerScore > secondPlayerScore:
            return "You win 😃"
        if firstPlayerScore == secondPlayerScore:
            return "Draw 🙃"
        return "You lose 😤"
    
    return isBusted

def blackjack(firstPlayerScore, secondPlayerScore):
    """Evaluate the player's score to determinate if there is a blackjack."""
    S_BLACKJACK = 22

    if firstPlayerScore == BLACKJACK and secondPlayerScore == BLACKJACK:
        return "Draw 🙃"
    if firstPlayerScore == BLACKJACK or firstPlayerScore == S_BLACKJACK:
        return "Win with a Blackjack 😎"
    if secondPlayerScore == BLACKJACK or secondPlayerScore == S_BLACKJACK:
        return "Lose, opponent has Blackjack 😱"
    
    return NO_WINNER
    
def busted(firstPlayerScore, secondPlayerScore):
    """Evaluate the player's scores to determinate if someone is busted."""
    if firstPlayerScore > 21:
        return "You went over. You lose 😤"
    if secondPlayerScore > 21:
        return "Opponent went over. You win 😁"
    return NO_WINNER

def blackjackOrBusted(firstPlayerScore, secondPlayerScore, newCardsCounter):
    """Return -1 for no winner, 0 for draw, 1 for first player winner and 2 for second player winner."""
    winner = NO_WINNER

    if newCardsCounter == 0:
        winner = blackjack(firstPlayerScore, secondPlayerScore)
    else:
        winner = busted(firstPlayerScore, secondPlayerScore)

    return winner

def dealerDecisions(firstPlayer, secondPlayer):
    """Dealer takes a desicion using player's scores."""
    firstPlayerScore = player.getScore(firstPlayer)
    secondPlayerScore = player.getScore(secondPlayer)
    players = []
    winnerString = ""
    
    while secondPlayerScore <= BLACKJACK:
        differenceOfBlackjack = abs(BLACKJACK - secondPlayerScore)
        
        if secondPlayerScore > firstPlayerScore:
            players = findWinner(firstPlayer, secondPlayer)
            return players
        
        if firstPlayerScore == secondPlayerScore:
            if differenceOfBlackjack in range(1, 4):
                players = findWinner(firstPlayer, secondPlayer)
                return players
            else:
                secondPlayerScore = drawNewCard(secondPlayer)
        else:
            secondPlayerScore = drawNewCard(secondPlayer)

    players = findWinner(firstPlayer, secondPlayer)
    return players

def drawNewCard(secondPlayer):
    player.getNewHand(secondPlayer)
    return player.getNewScore(secondPlayer)

def findWinner(firstPlayer, secondPlayer):
    """Returns a list with the winner and player's data."""
    firstPlayerScore = player.getScore(firstPlayer)
    secondPlayerScore = player.getScore(secondPlayer)
    players = []
    winnerString = ""

    winnerString =  winner(firstPlayerScore, secondPlayerScore)
    players.append(firstPlayer)
    players.append(secondPlayer)
    players.append(winnerString)
    return players