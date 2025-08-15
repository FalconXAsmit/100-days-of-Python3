# This is a simple tip calculator script.
# It prompts the user for the total bill amount, the tip percentage, number of people to split the bill.

# Text to tell the user what is this about.
print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

# Calculate the total amount including tip.
total_amount = total_bill + (total_bill * (tip_percentage / 100))

# Calculate the amount per person.
amount_per_person = total_amount / people_count

# Output the calculated amount per person to the user.
print(f"Each person should pay: ${amount_per_person: .2f}")