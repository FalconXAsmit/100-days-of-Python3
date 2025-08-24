# Blackjack Capstone Project Tutorial
import random


def deal_card():
    """Return a random card from the deck of cards"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Calculate the score of the cards in the list provided"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and len(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

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


print(f"Your final hand is: {user_cards}, and final score is: {user_score}")
print(f"Computer's final hand is: {computer_cards}, and final score is: {computer_score}")
compare(user_score, computer_score)

