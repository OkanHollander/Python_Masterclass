import sys


def my_range(n: int):
    start = 0
    while start < n:
        print(f"my_range is returning {start}")
        yield start
        start += 1


_ = input("line 11")
big_range = my_range(5)
print(f"big_range is {sys.getsizeof(big_range)}")
_ = input("line 14")
# create a list containing all the values in big_range
big_list = []
for val in big_range:
    big_list.append(val)

print(f"big_list is {sys.getsizeof(big_list)}")
