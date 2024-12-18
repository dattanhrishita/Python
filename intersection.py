# Define two lists
list1 = [15, 29, 33, 4, 7]
list2 = [4, 85, 67, 7, 8]

# Convert both lists to sets and perform the intersection
intersection = list(set(list1) & set(list2))

# Display the intersection
print("Intersection of the lists:", intersection)
