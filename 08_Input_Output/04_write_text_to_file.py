text_to_write = [
    "Line 1",
    "Line2",
    "Line3"
]

# file_name = "text_output.txt"

# # write to a file
# with open(file_name, "w") as f:
#     for line in text_to_write:
#         print(line, file=f)

# new_list = []
# with open(file_name, 'r') as f:
#     for line in f:
#         new_list.append(line)

# print(new_list)
file_name = "text_output.txt"
with open(file_name, "w") as f:
    for line in text_to_write:
        f.write(line + "\n")
