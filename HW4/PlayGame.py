from DeckOfCards import *
playing = True

while playing == True:
    #Welcomes player and initializes deck and scores
    print("Welcome to BlackJack!")
    print()
    deck = DeckOfCards()
    print("Here is the deck:")
    deck.print_deck()
    print()
    deck.shuffle_deck()
    print("Here is the shuffled deck")
    deck.print_deck()
    print()
    score = 0
    dealer_Score = 0
    busted = False

    #Initial Deal
    card = deck.get_card()
    card2 = deck.get_card()

    dealer = deck.get_card()
    dealer2 = deck.get_card()

    #Shows player their cards
    print(f"Card number 1 is: {card}")
    print(f"Card number 2 is: {card2}")
    print()

    #Sets scores and shows player their score
    dealer_Score += dealer.val
    dealer_Score += dealer2.val

    score += card.val
    score += card2.val
    print(f"Your total score is {score}")

    #Players game loop
    while busted == False:
        user_Input = input("Would you like to hit? (y/n): ")

        if user_Input == 'y':
            new_Card = deck.get_card()
            #Changes aces to ones if needed
            if score >= 11 and card.val == 11:
                # print(card.val, "This worked player 1")
                card.val = 1
                score -= 10
            if score >= 11 and card2.val == 11:
                # print(card2.val, "This worked player 2")
                card2.val = 1
                score -= 10
            if score >= 11 and new_Card.val == 11:
                # print(new_Card.val, "This worked player new")
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
                busted = True
            elif score == 21:
                print(f"Your score is {score}")
                print("BLACKJACK")
                break
        else:
            break

    #Dealers game loop
    print()
    print("OKAY, dealers turn")
    print()
    print(f"Dealer card number 1: {dealer}")
    print(f"Dealer card number 2: {dealer2}")
    print(f"Dealer's score is {dealer_Score}")
    print()
    card_Num = 2

    while dealer_Score < 21:
        card_Num += 1
        #Just to make sure the dealer doesn't get more cards if it already won
        if busted == True and dealer_Score < 21:
            print("Dealer wins")
            break
        if dealer_Score > score and dealer_Score < 21:
            print("You lost, dealer won")
            break
        else:
            new_Dealer = deck.get_card()
            print(f"Dealer card number {card_Num}: {new_Dealer}")
            print()
            #To change aces to ones if needed
            if dealer_Score >= 11 and dealer.val == 11:
                # print(dealer.val, "This worked")
                dealer.val = 1
                dealer_Score -= 10
            if dealer_Score >= 11 and dealer2.val == 11:
                # print(dealer2.val, "This worked 2")
                dealer2.val = 1
                dealer_Score -= 10
            if dealer_Score >= 11 and new_Dealer.val == 11:
                # print(new_Dealer.val, "This worked new_Dealer")
                new_Dealer.val = 1
            dealer_Score += new_Dealer.val
            print(f"Dealer's score is {dealer_Score}")
            if dealer_Score < 21 and dealer_Score < score:
                continue
            elif dealer_Score < 21 and dealer_Score > 17:
                if score > dealer_Score:
                    print("YOU WIN because dealer went over you")
                    break
                elif dealer_Score == score:
                    print("WOAH, that's a push")
                    break
                else:
                    print("You lose because dealer was better")
                    break
            elif dealer_Score == 21 and score < 21:
                print("DEALER GOT BLACKJACK, YOU SHOULD'VE HIT!")
            elif dealer_Score == 21 and score > 21:
                print("DEALER GOT BLACKJACK, YOU BUSTED!")
            elif dealer_Score == 21 and score == 21:
                print("Push")
            else:
                print("Dealer busted")
                break
    
    #Restarts or ends loop
    play_Again = input("Would you like to play again? (y/n): ")
    if play_Again == 'y':
        continue
    else:
        print("Thanks for playing!")
        playing == False
        break
