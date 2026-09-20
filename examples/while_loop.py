my_numbers = [4.23, 17.67, 1004, 1e-2]
my_var = 0
counter = 0

while my_var < 1000:
    my_var += my_numbers[counter]   # Index a list using square brackets
    counter += 1

print(my_var, counter)