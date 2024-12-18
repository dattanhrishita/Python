# Create a list
my_list = [12, 34, 5, 67, 4, 89, 1]

# Sort the list in ascending order
my_list.sort()

# Find the second smallest element
if len(my_list) > 1:
    second_smallest = my_list[1]
    print("Second smallest element is:", second_smallest)
else:
    print("There is no second smallest element in the list.")
