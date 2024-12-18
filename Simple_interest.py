#wap to calculate simple interest

# defining value of rate 
rate = 5

#taking input from user
principal = int(input("Enter the principal amount:"))
time = int(input("Enter the time:"))

#to calculate simple interest

simple_interest = (principal*rate*time)/100

#result
print("The simple interest is :",simple_interest)
