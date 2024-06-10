import random

# Define functions
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(hand):
    '''Take a list of cards - a hand - and returns the score'''

    if sum(hand) == 21 and len(hand) == 2:
        return 0  # score of zero will indicate that someone has a blackjack

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)

    return sum(hand)


# NOTE - order of if statements matter --> because the dealer gets priority for blackjack, that elif statement comes first. if it's true, then the if statement ends there
def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw, the Dealer wins this time"
    elif dealer_score == 0:
        return "The Dealer has Blackjack, you lost"
    elif player_score == 0:
        return "You got Blackjack! You win!"
    elif player_score > 21:
        return "You went over. You lose this time."
    elif dealer_score > 21:
        return "The Dealer busted. You win!"
    elif player_score > dealer_score:
        return "You beat the Dealer!"
    else:
        return "You lose."


def play_blackjack():
    player_hand = []
    dealer_hand = []
    is_game_over = False

    # deal initial cards
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True

        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == 'y':
                player_hand.append(deal_card())
            else:
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
    play_blackjack()