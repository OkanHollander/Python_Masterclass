import random

def get_integer(prompt):
    """
    Prompt (str): The prompt to display to the user.
    
    The function will continue looping, and prompting
    the user, until a valid 'int' is entered.
    
    :param prompt: The prompt to display to the user.
    :return: The integer entered
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print(f"{temp} is not a valid integer.")


guess = 0
answer = input("enter integer")
while guess != answer:
    guess = get_integer(answer)
    if guess == answer:
        print("you win!")
        break
    else:
        if guess < answer:
            print("too small")
        else:
            print("too big")