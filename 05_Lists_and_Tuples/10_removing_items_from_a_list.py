available_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'hdmi cable']
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:

        index = int(current_choice)
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            computer_parts.remove(chosen_part)
            print(f"Removing {current_choice}")
        else:
            computer_parts.append(chosen_part)
            print(f"Adding {current_choice}")
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list below:")
        for number, option in enumerate(available_parts):
            print(f"{number + 1}: {option}")
        print("0: to exit")
    current_choice = input()
print(computer_parts)
