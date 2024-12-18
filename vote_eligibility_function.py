# Define a function to check if a person can vote
def can_vote(age):
    # Return True if age is 18 or above, otherwise False
    return age >= 18

# Ask the user to input their age
age = int(input("Enter your age: "))

# Check the vote eligibility using the function
if can_vote(age):
    # If the function returns True, print eligible message
    print("You are eligible to vote.")
else:
    # If the function returns False, print not eligible message
    print("You are not eligible to vote.")
