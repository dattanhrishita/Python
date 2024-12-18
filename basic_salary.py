'''
WAP to accept basic salary from user and Give 10% of DA on basic salary ,
12% HRA on basic salary  to employee if the salary is more than 50000 .
calculate total salary.
'''

#taking input from user
basic_salary = float (input ("Enter the basic salary: "))

#Initialize DA and HRA 
da = 0
hra = 0
#To checking if the basic salary is more than 50000
if basic_salary > 50000:
    # Calculating 10% DA on basic salary
    da = 0.10 * basic_salary
    
    # Calculating 12% HRA on basic salary
    hra = 0.12 * basic_salary

    
#Calculating the total salary
total_salary= basic_salary + da + hra
    
#Displaying the total salary
print ("Total Salary: ", total_salary)
