import random

# Card values
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def create_deck():
    return [(v, s) for v in values for s in suits]

def deal_card(deck):
    return deck.pop(random.randint(0, len(deck) - 1))

def hand_value(hand):
    nums = [int(card[0]) for card in hand]
    return sum(nums)

def show_hand(player, hand):
    print(f"{player}'s hand:")
    for card in hand:
        print(f"{card[0]} of {card[1]}")
    print(f"Total value: {hand_value(hand)}\n")

def play_game():
    deck = create_deck()

    player_hand = [deal_card(deck), deal_card(deck)]
    computer_hand = [deal_card(deck), deal_card(deck)]

    print("Welcome to Simple Poker!\n")

    # Player turn
    while True:
        show_hand("Your", player_hand)
        choice = input("Hit or stand? (h/s): ").lower()

        if choice == 'h':
            player_hand.append(deal_card(deck))
            if hand_value(player_hand) > 21:
                print("You busted! Computer wins.")
                return
        else:
            break

    # Computer turn
    while hand_value(computer_hand) < 17:
        computer_hand.append(deal_card(deck))

    show_hand("Computer", computer_hand)

    # Decide winner
    player_total = hand_value(player_hand)
    computer_total = hand_value(computer_hand)

    if computer_total > 21 or player_total > computer_total:
        print("You win!")
    elif player_total < computer_total:
        print("Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()
