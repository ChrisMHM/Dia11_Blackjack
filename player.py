import cardsController
import hand

deck = cardsController.cards

hand = hand.getInitialHand(deck)

print(f"initial hand: {hand}")