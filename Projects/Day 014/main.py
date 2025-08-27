# Higher Lower Game

import os
import random
from game_data import data
from art import logo, vs

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def game():
    score = 0
    game_over = False

    choice_a = random.choice(data)
    choice_b = random.choice(data)
    while choice_a == choice_b:
        choice_b = random.choice(data)

    while not game_over:
        print(logo)
        print(f"Compare A: {choice_a['name']}, a {choice_a['description']} from {choice_a['country']}")
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']} from {choice_b['country']}")

        guess = input("Who have more insta followers? Type 'A' or 'B':  ").lower()
        a_followers = choice_a['follower_count']
        b_followers = choice_b['follower_count']
        
        is_correct = (guess == 'a' and a_followers > b_followers) or (guess == 'b' and b_followers > a_followers)

        clear()

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
            choice_a = choice_b
            choice_b = random.choice(data)
            while choice_a == choice_b:
                choice_b = random.choice(data)
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final Score: {score}")

game()
