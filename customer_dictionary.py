'''
WAP to create dictionaries for below task and perform all the above operations on it.

Each customer ID in a company is associated with a customer name.
'''

#crating a dictionary products
customers = {
    101: "Andrew",
    102: "Matt",
    103: "Riko",
    104: "Kevin"
}




#prints the dictionary
print("The customer ID and names are :",customers)

#price of a specified dictionary value 
print("Name of customer with ID: ",customers[103])

#storing the value in a variable and displaying  
y=customers[104]
print("Name of customer :",y)

#Adding new element to the dictionary
customers[105]="Allison"
print("After adding new element: ",customers)

#updating name of customer
#before updation
print(" before updation :",customers[101])

customers.update({101:"Aaron"})
print(" after updation: ",customers[101])

#finding all keys present in the dictionary
k=customers.keys()
print("The keys are : ",k)

#Remove Neil from the dictonary
customers.pop(102)
print("Dictionary after removing customer id 102 :",customers)


#looping over dictionary
for i in customers:
    print(i)

#to get keys from the dictionary
    for i in customers.keys():
        print(i)

#to get values from the dictionary
for i in customers.values():
    print(i)
