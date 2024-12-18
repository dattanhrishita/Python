list_a=[]


for i in range(5):
    element = input("Enter element:")
    list_a.append(element)

print("The list created is :",list_a)

new_element=input("Enter a new element: ")
list_a.append(new_element)

print("List after insertion :",list_a)


delete_position = int(input("Enter the position of the element to delete: "))
list_a.pop(delete_position)

print("List after deletion:",list_a)
