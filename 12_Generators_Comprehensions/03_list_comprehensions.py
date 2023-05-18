print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

# nornal for loop
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares)

# list comprehension
squares = [number ** 2 for number in numbers]
print(squares)

text = "what have the romans ever done to us"
capitals = [letter.upper() for letter in text]
print(capitals)

