# Tip Calculator

This project is a practical tool to calculate the tip for a bill and split it among a number of people. It takes the total bill, the desired tip percentage, and the number of people as input, then calculates how much each person should pay.

---

### Key Concepts Practiced

This project was a great exercise in handling different data types and performing calculations.

#### 1. Data Types & Type Casting

The `input()` function always returns a **string**. To perform mathematical calculations, we need to convert these strings into numbers.

* `float()`: Used to convert the total bill and tip percentage into floating-point numbers (numbers with decimals). This is important for handling currency accurately.
* `int()`: Used to convert the number of people into an integer (a whole number).

```python
# input() gives us a string, e.g., "150.00"
bill = float(input("What was the total bill? $")) 

# Convert the tip percentage to an integer
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
```

#### 2. Mathematical Operations

The project involved several key calculations:
* Calculating the tip amount by converting the percentage to a decimal (`tip_percentage / 100`).
* Calculating the total bill including the tip.
* Dividing the total by the number of people to get the individual share.

```python
# Calculate the actual tip amount
tip_amount = bill * (tip_percentage / 100)
total_bill = bill + tip_amount

# Calculate the share per person
per_person_share = total_bill / num_people
```

#### 3. f-Strings for Formatting Output

**f-Strings** are use to embed expressions inside string literals. They were crucial for formatting the final output to look like currency (with two decimal places).

The format specifier `:.2f` tells Python to format the number as a float with exactly two decimal places.

```python
# Round the result to 2 decimal places for currency
final_amount = "{:.2f}".format(per_person_share)

# Use an f-string to present the final result clearly
print(f"Each person should pay: ${final_amount}")

### Key Takeaways 