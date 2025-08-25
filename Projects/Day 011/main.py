# Blackjack Capstone Project
# importing required modules
import random
import os 

# To Clear the terminal
def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# To deal the cards to both computer and user
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

# To calculate the scores of computer and user
def calculate_score(cards):
    if sum(cards) == 21 and sum(cards) == 2:
        return 0
    if 11 in cards and len(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# To compare the user and computer scores to determine who won
def compare(user, computer):
    if user == computer:
        return "Draw 😑"
    elif computer == 0:
        return "Lose, Opponent has a BlackJack 😱"
    elif user == 0:
        return "Win, With a BlackJack 🥳"
    elif user > 21:
        return "You went over 21, you lose 😭"
    elif computer > 21:
        return "Opponent went over, You Win 😁"
    elif user > computer:
        return "You win 😀"
    else:
        return "You lose 🥲"

# Main game logic
def play_game():
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, Current score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to hit or type 'n' to stand: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is: {user_cards}, and final score is: {user_score}")
    print(f"Computer's final hand is: {computer_cards}, and final score is: {computer_score}")
    print(compare(user_score, computer_score))

# Logo for my game
logo = '''
.===================================================================.
|               _   _   _   _   _   _   _   _   _                   |
|              / \ / \ / \ / \ / \ / \ / \ / \ / \                  |
|             ( B | L | A | C | K | J | A | C | K )                 |
|              \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/                  |
|                                                                   |
|                      - By FalconXAsmit -                          |
|                                                                   |
|         .--------.                               .---------.      |
|         | A      |                               | J       |      |
|         | ♠      |                               | ♣       |      |
|         |        |                               |         |      |
|         |    ♠   |                               |    ♣    |      |
|         |        |                               |         |      |
|         |      ♠ |                               |       ♣ |      |
|         |      A |                               |       J |      |
|         '--------'                               '---------'      |
|                                                                   |
'==================================================================='
'''

# To gamble my life away with again and again
while input("Do you want to play a game od blackjack? 'y' or 'n' ") == 'y':
    clear()
    print(logo)
    play_game()
