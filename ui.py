import art
import player

logo  = art.logo

#Player data
gamer = player.getPlayer()
gamerHand = player.getHand(gamer)
gamerScore = player.getScore(gamer)
newGamerScore = 0

#Dealer data
dealer = player.getPlayer()
dealerHand = player.getHand(dealer)
dealerScore = player.getScore(dealer)
dealerFirstCard = player.getFirstCard(dealer)


# playAGame = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
playAGame = "y"

if playAGame == "y":
    print(logo)     
    print(f"Your cards: {gamerHand}, current score: {gamerScore}")
    print(f"Dealer cards: {dealerHand}, current score: {dealerScore}")
    print(f"Computer's first card: {dealerFirstCard}")
    # anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
    anotherCard = "y"
    if anotherCard == "y":
        gamerHand = player.newHand(gamerHand)
        newGamerScore = player.getScore(gamer)
        player.setScore(gamer, newGamerScore)
        gamerScore = player.getScore(gamer)

        print(f"Your cards: {gamerHand}, current score: {gamerScore}")
        print(f"Dealer cards: {dealerHand}, current score: {dealerScore}")
        print(f"Computer's first card: {dealerFirstCard}")