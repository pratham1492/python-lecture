print("PROJECT : FUNDAMENTAL BOOSTER")
print("Welcome to the interactive personal data collector!")

#personal data infromation.

#input user details.

name = input("Enter your name:")
age = input("Enter your age:")
height = input("Enter your height:")
contact = input("Enter your contact:")

print("Thank you! I've have collected your infromation.")

print("name:",name)
print("age:",age)
print("height:",height)
print("contact:",contact)

#collecting information.

name = "pratham chauhan"
age = 18
height = 181
contact = 9099419589

# using type function to finding data types

print(type(name))
print(type(age))
print(type(height))
print(type(contact))

# calculatating birth year from age.

current_year = 2025
birth_year = current_year-age

print("your birth is:",birth_year)



# (concatenation) means adding by format function.

message = f"{name} you are born in {birth_year} based on your age"
print(message)



#type casting converting types from int to float and float to int.

age = float(age)
print("age:",age)
print(type(age))

height= int(height)
print("height:",height)
print(type(height))




# address memory location using id() function.

print("name:",id(age))
print("age:",id(age))
print("height:",id(height))
print("contact:",id(contact))




print("Thanks for using personal data collector.Goodbye!")
