# Band Name Generator

This is a simple project that will generate a band name based on some questions answered by the user.

For example:- 
* What's the name of the city you grew up in?
* What's the name of your pet?

```python
city_name = input("What's the name of the city you grew up in?\n")
pet_name = input("What's the name of your pet?\n")
```

Then it will combine the answer of these question given by the user and print the following band name. 

```python
band_name = city_name + " " + pet_name
print("Your band name could be " + band_name)
```

We can also print it by using f-strings like

```python
print(f"Your band name could be {band_name}")
```

## Key Takeaways
* **User Input**:- Used the `input()` function to get data from the user.
* **String Concatenation**:- Combined the `city_name` and `pet_name` strings to create the final `band_name`.
* **Variables**:- Stored the user's input and the final result in variables.