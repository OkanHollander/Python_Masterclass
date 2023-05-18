print(__file__)

number = int(input("How many items do you want to generate?"))
numbers = [1, 2, 3, 4, 5, 6]
squares = [number**2 for number in numbers]

index_position = numbers.index(number)
print(squares[index_position])
