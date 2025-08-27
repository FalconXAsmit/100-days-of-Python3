# Higher Lower Game

import os
import random

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

data = [
    {
        'name': 'Instagram',
        'follower_count': 672,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 631,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 503,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 429,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 400,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Dwayne "The Rock" Johnson',
        'follower_count': 398,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 380,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 364,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 319,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 311,
        'description': 'Reality TV personality and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Nike',
        'follower_count': 306,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 293,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 283,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 222,
        'description': 'Footballer',
        'country': 'Brasil'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 269,
        'description': 'Cricketer',
        'country': 'India'
    }
]

choice_1 = random.choice(data)
choice_2 = random.choice(data)
score = 0
game_over = False

while choice_1 == choice_2:
    choice_2 = random.choice(data)

print(f"Compare A: {choice_1['name']}, a {choice_1['description']} from {choice_1['country']}")
print("vs")
print(f"Compare B: {choice_2['name']}, a {choice_2['description']} from {choice_2['country']}")

guess = input("Who have more insta followers? Type 'A' or 'B':  ").lower()

clear()

if guess == 'a':
    if choice_1['follower_count'] > choice_2['follower_count']:
        score += 1
    else:
        print(f"Sorry, thats wrong. Final Score: {score}")
        game_over = True
elif guess == 'b':
    if choice_2['follower_count'] > choice_1['follower_count']:
        score += 1
    else:
        print(f"Sorry, thats wrong. Final Score: {score}")
        game_over = True

while not game_over:
    choice_2 = random.choice(data)
    while choice_1 == choice_2:
        choice_2 = random.choice(data)

    print(f"Compare A: {choice_1['name']}, a {choice_1['description']} from {choice_1['country']}")
    print("vs")
    print(f"Compare B: {choice_2['name']}, a {choice_2['description']} from {choice_2['country']}")
    print(f"You're right! Current Score: {score}")

    guess = input("Who have more insta followers? Type 'A' or 'B':  ").lower()
    clear()

    if guess == 'a':
        if choice_1['follower_count'] > choice_2['follower_count']:
            score += 1
        else:
            print(f"Sorry, thats wrong. Final Score: {score}")
            game_over = True
    elif guess == 'b':
        if choice_2['follower_count'] > choice_1['follower_count']:
            score += 1
        else:
            print(f"Sorry, thats wrong. Final Score: {score}")
            game_over = True
