computer_parts = {"1": 'computer',
                  "2": 'monitor',
                  "3": 'keyboard',
                  "4": 'mouse',
                  "5": 'printer',
                  "6": 'cd-rom',
                  "7": 'mouse mat'}

current_choice = None
while current_choice != "0":
    if current_choice in computer_parts:
        chosen_part = computer_parts[current_choice]
        print(f"Adding ~~{chosen_part}~~ to your computer.")
        print("")
    current_choice = input("Please choose a part: ")
