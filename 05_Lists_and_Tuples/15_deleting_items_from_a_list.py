data = [4, 5, 104, 105, 110, 120, 130, 150,
        160, 170, 183, 185, 188, 191, 350, 360]

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
# print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)
del data[:stop]
print(data)
