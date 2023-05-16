available_parts = ['computer', 'monitor', 'keyboard', 'mouse', 'mouse mat', 'hdmi cable']
current_choice = "-"
computer_parts = []  # create an empty list

while current_choice != '0':
    if current_choice in "123456":
        print(f"Adding {current_choice}")
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append('monitor')
        elif current_choice == '3':
            computer_parts.append('keyboard')
        elif current_choice == '4':
            computer_parts.append('mouse')
        elif current_choice == '5':
            computer_parts.append('mouse mat')
        elif current_choice == '6':
            computer_parts.append('hdmi cable')
    else:
        print("Please add options from the list below:")
        for option in available_parts:
            print(f"{available_parts.index(option)+1}: {option}")
            print("0: to exit")
    current_choice = input()
print(computer_parts)
