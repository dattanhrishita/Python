'''
WAP to create dictionaries for below task and perform all the above operations on it.

Each product in a supermarket is associated with its price.
'''

#creating a dictionary products
products={"Banana":250,
          "Tomato":100,
          "Carrot":50,
          "Milk":25,
          "Soap":45
          }

#prints the dictionary
print("The products and theirs prices are :",products)

#price of a specified dictionary value 
print("Price of banana: ",products["Banana"])

#storing the value in a variable and displaying  
y=products["Carrot"]
print("Prices of carrot :",y)

#Adding new element to the dictionary
products["Juice"]=76
print("After adding new element: ",products)

#updating a Soap price
#before updation
print("Price of soap before updation :",products["Soap"])

products.update({"Soap":150})
print("Price of soap after updation: ",products["Soap"])

#finding all keys present in the dictionary
k=products.keys()
print("The keys are : ",k)

#Remove tomato from the dictonary
products.pop("Tomato")
print("Dictionary after removing tomato :",products)


#looping over dictionary
for i in products:
    print(i)

#to get keys from the dictionary
for i in products.keys():
        print(i)

#to get values from the dictionary
for i in products.values():
    print(i)
