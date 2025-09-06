PLACEHOLDER = "[name]"

with open(r"Projects\Day 024\Input\Names\invited_names.txt") as names_file:
    names = names_file.readlines()

with open(r"Projects\Day 024\Input\Letters\starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, name)
        with open(f"Projects/Day 024/Output/Ready To Send/letter_for_{name}.docx", mode="w") as completed_letter:
            completed_letter.write(new_letter)
