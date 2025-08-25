# A Secret Auction
# Importing os module to clear the screen for the next bidder to not know what the previous bidder have bid
import os

# Function to clear the terminal cls is for Windows and clear for MacOS and Linux Operating Systems
def clear():
    if os.name == "nt":
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# To find out who is the highest bidder
def highest_bid_winner(bids):
    winner = ""
    highest_bid = 0
    for bidder in bids:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"This auction is won by {winner} with a bid of ${highest_bid}")

# ASCII art of auction
logo= '''
     ___________
     \         /
      )_______(
      |"""""""|_.-._,.---------.,_.-._
      |       | | |               | | ''-.
      |       |_| |_             _| |_..-'
      |_______| '-' `'---------'` '-'
      )"""""""(
     /_________\
     
   .-------------.
  /_______________\
'''

print(logo)
print("Welcome to my secret auction.")
bidders = {}

# Main logic of filling up the dictionary
program_over = False
while not program_over:
    name = input("What is your Name?:")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    to_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if to_continue == 'no':
        program_over = True
        highest_bid_winner(bidders)
    clear()
