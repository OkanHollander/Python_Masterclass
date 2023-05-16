user_input = input("Please enter 3 numbers, seperated by comma(,)")
string_list = user_input.split(str(","))
number_list = []
for number in string_list:
    number_list.append(int(number))
print(number_list)
a,b,c = number_list
output = a+b-c
print(output)