import art
import player
import gameFunctionality
import clear

logo  = art.logo
newCardsCounter = 0
NO_WINNER = ""

#Player data
firstPlayer = player.getPlayer()
firstPlayerHand = player.getHand(firstPlayer)
firstPlayerScore = player.getScore(firstPlayer)

#Dealer data
dealer = player.getPlayer()
dealerHand = player.getHand(dealer)
dealerScore = player.getScore(dealer)
dealerFirstCard = player.getFirstCard(dealer)

playAGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
again = True

while playAGame == "y":
    clear.clear()

    print(logo)     

    while again:
        gameFunctionality.printPlayersInfo(firstPlayerHand, firstPlayerScore, dealerHand, dealerScore, dealerFirstCard)

        blackjackBustedResult = gameFunctionality.blackjackOrBusted(firstPlayerScore, dealerScore, newCardsCounter)
        newCardsCounter += 1

        if blackjackBustedResult != NO_WINNER:
            gameFunctionality.printFinalPlayersInfo(firstPlayer, dealer)
            print(blackjackBustedResult)
            again = False
        else:
            anotherCard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            
            if anotherCard == "y":
                firstPlayerHand = player.getNewHand(firstPlayer)
                firstPlayerScore = player.getNewScore(firstPlayer)

            else:
                playersStatus = gameFunctionality.dealerDecisions(firstPlayer, dealer)
                firstPlayer = playersStatus[0]
                dealer = playersStatus[1]
                resultString = playersStatus[2]
                gameFunctionality.printFinalPlayersInfo(firstPlayer, dealer)
                print(resultString)
                again = False

    playAGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if playAGame == "y":
        again = True
        newCardsCounter = 0
        #Player data
        firstPlayer = player.getPlayer()
        firstPlayerHand = player.getHand(firstPlayer)
        firstPlayerScore = player.getScore(firstPlayer)

        #Dealer data
        dealer = player.getPlayer()
        dealerHand = player.getHand(dealer)
        dealerScore = player.getScore(dealer)
        dealerFirstCard = player.getFirstCard(dealer)
    else:
        again = False 
        print("Bye")

print("Game finished!")