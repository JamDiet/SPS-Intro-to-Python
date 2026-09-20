"""
In general, a for loop iterates through items of a list:

    for ELEMENT in LIST:
        ...
"""


my_numbers = [4.23, 17.67, 1004, 1e-2]
my_var = 0

for num in my_numbers:
    my_var += num   # The += operator adds the value on the right to the current value of the variable on the left

print(my_var)