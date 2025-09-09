import pandas as pd

raw_data = pd.read_csv("Extra_Files/Day_025.csv")

grey = len(raw_data[raw_data["Primary Fur Color"] == "Gray"])
cinnamon = len(raw_data[raw_data["Primary Fur Color"] == "Cinnamon"])
black = len(raw_data[raw_data["Primary Fur Color"] == "Black"])

print(grey)
print(cinnamon)
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, cinnamon, black],
}

print(data_dict)

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
