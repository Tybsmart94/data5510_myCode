from DeckOfCards import *

print("Welcome to BlackJack!")
deck = DeckOfCards()
deck.shuffle_deck()
score = 0
dealer_Score = 0

#Initial Deal
card = deck.get_card()
card2 = deck.get_card()

dealer = deck.get_card()
dealer2 = deck.get_card()

print(f"Card number 1 is: {card}")
print(f"Card number 2 is: {card2}")
print()

dealer_Score += dealer.val
dealer_Score += dealer2.val

score += card.val
score += card2.val
print(f"Your total score is {score}")

while score < 21:
    #Game loop
    user_Input = input("Would you like to hit? (y/n): ")

    if user_Input == 'y':
        new_Card = deck.get_card()
        if score >= 11 and new_Card.val == 11:
            new_Card.val = 1
        print()
        print(f"Card number 3 is: {new_Card}")
        score += new_Card.val
        print(f"Your total score is {score}")
        print()

        if score < 21:
            continue
        elif score > 21:
            print(f"Your score is {score}")
            print("YOU LOSE")
            print()
            break
        else:
            print(f"Your score is {score}")
            print("BLACKJACK")
            break
    else:
        print()
        print("OKAY, dealers turn")
        print()
        break

while dealer_Score < 21:
    print(f"Dealer card number 1: {dealer}")
    print(f"Dealer card number 2: {dealer2}")
    dealer3 = deck.get_card()
    dealer_Score += dealer3.val
    print(f"Dealer card number 3: {dealer3}")
    print(f"Dealer's score is {dealer_Score}")
    print()

    if dealer_Score < 21:
        dealer4 = deck.get_card()
        print(f"Dealer card number 4: {dealer4}")
        dealer_Score += dealer4.val
        print(f"Dealer's score is {dealer_Score}")
        print()
        if dealer_Score < 21 and dealer_Score > 17:
            if score > dealer_Score:
                print("YOU WIN because dealer went over you")
                break
            else:
                print("You lose because dealer was better 2")
                break
        elif dealer_Score < 21 and dealer_Score < 17:
            dealer5 = deck.get_card()
            print(f"Dealer card number 5: {dealer5}")
            dealer_Score += dealer5.val
            print(f"Dealer's score is {dealer_Score}")
        else:
            print("Dealer loses because he did")
            break
    else:
        print("Dealer busted")
        break
