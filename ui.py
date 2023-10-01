import art
import player
import gameFunctionality

logo  = art.logo

#Player data
firstPlayer = player.getPlayer()
firstPlayerHand = player.getHand(firstPlayer)
firstPlayerScore = player.getScore(firstPlayer)

#Dealer data
dealer = player.getPlayer()
dealerHand = player.getHand(dealer)
dealerScore = player.getScore(dealer)
dealerFirstCard = player.getFirstCard(dealer)

# playAGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
playAGame = "y"
again = True

if playAGame == "y":
    print(logo)     

    while again:
        anotherCard = gameFunctionality.printPlayersInfo(firstPlayerHand, firstPlayerScore, dealerHand, dealerScore, dealerFirstCard)
        
        if anotherCard == "y":
            firstPlayerHand = player.getNewHand(firstPlayer, firstPlayerHand)
            firstPlayerScore = player.getNewScore(firstPlayer)
        else:
            again = False