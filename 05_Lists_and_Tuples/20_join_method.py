data = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "bacon"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
VALUE_TO_REMOVE = 'spam'
for sublist in data:
    for value in sublist.copy():
        if value == VALUE_TO_REMOVE:
            sublist.remove(value)
    print(", ".join(sublist))

print('*'*80)
flowers = [
    "daffodil",
    "evening primrose",
    "hydrangea",
    "iris",
    "lavender",
    "sunflower",
    "tiger lilly"
]

seperator = " | "
output = seperator.join(flowers)
print(output)
