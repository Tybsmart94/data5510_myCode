#Imports and marker variable
from DeckOfCards import *
playing = True

#Welcome message only to be played once
print("Welcome to BlackJack!")
print()

#Entire game loop
while playing == True:
    #Initialization of deck
    deck = DeckOfCards()

    #Prints unshuffled and shuffled decks
    print("Here is the deck:")
    deck.print_deck()
    print()
    deck.shuffle_deck()
    print("Here is the shuffled deck")
    deck.print_deck()

    #initializes scores and busted variable
    print()
    score = 0
    dealer_Score = 0
    busted = False

    #Initial Deals for player and dealer
    card = deck.get_card()
    card2 = deck.get_card()

    dealer = deck.get_card()
    dealer2 = deck.get_card()

    #Shows player their cards and the dealer's first card
    print(f"Card number 1 is: {card}")
    print(f"Card number 2 is: {card2}")
    print()
    print(f"The dealers first card is {dealer}")
    print()

    #Sets scores
    dealer_Score += dealer.val
    dealer_Score += dealer2.val

    score += card.val
    score += card2.val

    #Counter variable
    card_Num_Player = 2

    #Ends game if player gets blackjack
    if score == 21 and dealer_Score != 21:
        print("CONGRATS, you got blackjack")
        #Restarts or ends loop
        play_Again = input("Would you like to play again? (y/n): ")
        if play_Again == 'y':
            continue
        else:
            print("Thanks for playing!")
            playing == False
            break

    #Ends game if dealer already has BlackJack
    if dealer_Score == 21 and score != 21:
        print(f"Dealers Cards: {dealer}, {dealer2}")
        print("Dealer got blackjack, sorry loser")
        #Restarts or ends loop
        play_Again = input("Would you like to play again? (y/n): ")
        if play_Again == 'y':
            continue
        else:
            print("Thanks for playing!")
            playing == False
            break
    
    #Shows you your score
    print(f"Your total score is {score}")

    #Players game loop
    while busted == False:
        card_Num_Player += 1

        user_Input = input("Would you like to hit? (y/n): ")

        #Hit game loop
        if user_Input == 'y':
            new_Card = deck.get_card()
            score += new_Card.val

            #Changes aces to ones if needed
            if score > 21 and card.val == 11:
                # print(card.val, "This worked player 1")
                score -= 10
            if score > 21 and card2.val == 11:
                # print(card2.val, "This worked player 2")
                score -= 10
            if score > 21 and new_Card.val == 11:
                # print(new_Card.val, "This worked player new")
                score -= 10
            
            #Updates the player on their standing
            print()
            print(f"Card number {card_Num_Player} is: {new_Card}")
            print(f"Your total score is {score}")
            print()

            #Checks score to see if player can keep going or should move on
            if score < 21:
                continue
            elif score > 21:
                print(f"Your score is {score}")
                # print("YOU LOSE")
                print()
                busted = True
            elif score == 21:
                print(f"Your score is {score}")
                # print("BLACKJACK")
                break
        
        #Ends players loop so dealer can start
        else:
            break

    #Dealers game loop
    print("Dealers turn")
    print()
    print(f"Dealer card number 1: {dealer}")
    print(f"Dealer card number 2: {dealer2}")
    print(f"Dealer's score is {dealer_Score}")
    print()

    #Counter variable
    card_Num = 2

    #Dealers hit loop
    while dealer_Score < 21:
        card_Num += 1

        #Just to make sure the dealer doesn't get more cards if it already won
        if busted == True and dealer_Score < 21:
            print("Dealer wins")
            break
        #Makes sure that the dealer won't continue playing if it is closer to 21 than us
        elif dealer_Score > score and dealer_Score < 21:
            print("You lost, dealer won")
            break
        #Actual hit loop
        else:
            new_Dealer = deck.get_card()
            dealer_Score += new_Dealer.val

            #To change aces to ones if needed
            if dealer_Score > 21 and dealer.val == 11:
                # print(dealer.val, "This worked")
                dealer_Score -= 10
            if dealer_Score > 21 and dealer2.val == 11:
                # print(dealer2.val, "This worked 2")
                dealer_Score -= 10
            if dealer_Score > 21 and new_Dealer.val == 11:
                # print(new_Dealer.val, "This worked new_Dealer")
                dealer_Score -= 10

            #Updates player on dealer's standing
            print(f"Dealer card number {card_Num}: {new_Dealer}")
            print()
            print(f"Dealer's score is {dealer_Score}")

            #Checks scores to see if dealer can continue
            if dealer_Score < 21 and dealer_Score < score:
                continue
            elif dealer_Score < 21 and dealer_Score > 17:
                if score > dealer_Score:
                    print("YOU WIN because you were closer to 21")
                    break
                elif dealer_Score == score:
                    print("Push")
                    break
                else:
                    print("You lose because dealer was closer to 21")
                    break
            
            #Special conditions + Most common condition in else
            elif dealer_Score == 21 and score < 21:
                print("DEALER GOT BLACKJACK, YOU SHOULD'VE HIT!")
                break
            elif dealer_Score == 21 and score > 21:
                print("DEALER GOT BLACKJACK, YOU BUSTED!")
                break
            elif dealer_Score == 21 and score == 21:
                print("YOU BOTH GOT BLACKJACK??? Crazy")
                break
            else:
                print("Dealer busted, you win")
                break
    
    #Restarts or ends loop
    play_Again = input("Would you like to play again? (y/n): ")
    if play_Again == 'y':
        continue
    else:
        print("Thanks for playing!")
        playing == False
        break
