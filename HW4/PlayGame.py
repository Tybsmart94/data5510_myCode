from DeckOfCards import *

print("Welcome to BlackJack!")
deck = DeckOfCards()
deck.shuffle_deck()
score = 0


while score < 21:
    #Initial Deal
    card = deck.get_card()
    card2 = deck.get_card()

    print(card, card2)

    score += card.val
    score += card2.val

    print(f"Your score is {score}")

    #Game loop
    user_Input = input("Would you like to hit? (y/n): ")

    if user_Input == 'y':
        card3 = deck.get_card()
        score += card3.val

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
        print(f"Your score is {score}, wimp")
        break