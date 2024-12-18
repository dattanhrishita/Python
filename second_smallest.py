# Create a list
my_list = [12, 34, 5, 67, 4, 89, 1]

# Remove duplicates by converting the list to a set
new_list = list(set(my_list))

# Sort the list in ascending order
new_list.sort()

# Find the second smallest element
if len(new_list) > 1:
    second_smallest = new_list[1]
    print("Second smallest element is:", second_smallest)
else:
    print("There is no second smallest element in the list.")
