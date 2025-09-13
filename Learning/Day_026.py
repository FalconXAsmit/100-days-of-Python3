import pandas as pd

# List Comprehension

# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n +1
#     new_list.append(add_1)
# print(new_list)

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)

student_dict = {"student": ["Asmit", "Lily", "Joker"], "score": [76, 69, 98]}

student_df = pd.DataFrame(student_dict)
print(student_df)

for (index, row) in student_df.iterrows():
    print(row)
