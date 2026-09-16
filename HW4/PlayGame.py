from DeckOfCards import *

print("Welcome to BlackJack!")
deck = DeckOfCards()
deck.shuffle_deck()
score = 0
hand = []
dealer_Hand = []

#Initial Deal
card = deck.get_card()
hand.append(card.val)
card2 = deck.get_card()
hand.append(card2.val)

dealer = deck.get_card()
dealer_Hand.append(dealer.val)
dealer2 = deck.get_card()
dealer_Hand.append(dealer2.val)


print("Your Hand")
print(f"{card}, {card2}")
print(hand)
print()

print("Dealer hand")
print(f"{dealer}")

score += card.val
score += card2.val
print(f"Your score is {score}")
print()

while score < 21:
    #Game loop
    user_Input = input("Would you like to hit? (y/n): ")

    if user_Input == 'y':
        new_Card = deck.get_card()
        if score >= 11 and new_Card.val == 11:
            new_Card.val = 1
        print()
        print(f"{card}, {card2}, {new_Card}")
        score += new_Card.val
        hand.append(new_Card.val)
        print(f"Your score is {score}")
        print()
        print(hand)
        print()

        if score < 21:
            print(f"Your score is {score}")
            continue
        elif score > 21:
            print(f"Your score is {score}")
            print("YOU LOSE")
            break
        else:
            print(f"Your score is {score}")
            print("BLACKJACK")
            break
    else:
        print(f"{dealer}, {dealer2}")
        dealer3 = deck.get_card()
        dealer_Hand.append(dealer3.val)
