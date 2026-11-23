# ASSIGNMENT TASK 1 - UNIT 1
# Combined Python programs (Tasks 1-18)

# Task 1: Print name, department, and college on separate lines
print("Hemant")
print("Computer Science and Engineering")
print("JAIN UNIVERSITY")


# Task 2: Print the pattern
print("*******")
print("*******")
print("*******")


# Task 3: Print a sentence using a single print() statement
print("Python is Easy")


# Task 4: Print the number pattern
print("1")
print("12")
print("123")
print("1234")
print("12345")


# Task 5: Use \n to print words on separate lines
print("Computer\nScience\nEngineering")


# Task 6: Use \t to print values separated by tabs
print("Name\tAge\tCity")


# Task 7: Single-line comment and welcome message
# This program prints a welcome message.
print("Welcome to Python")


# Task 8: Multi-line comment
"""
This is a multi-line comment.
It explains the purpose of the program.
"""
print("Hello, Python!")


# Task 9: Three comments and three print statements
# Print the first message
print("Hello")

# Print the second message
print("Welcome")

# Print the third message
print("Python is Easy")


# Task 10: Store and print a name
name = "Hemant"
print(name)


# Task 11: Store three numbers in different variables and print them
a = 10
b = 20
c = 30
print(a)
print(b)
print(c)


# Task 12: Convert a string into an integer and display its value and type
value = "100"
number = int(value)
print(number)
print(type(number))


# Task 13: Convert an integer into a float and display the result and type
number = 25
result = float(number)
print(result)
print(type(result))


# Task 14: Accept the user's age and display it
age = int(input("Enter your age: "))
print(age)


# Task 15: Accept two numbers and display their sum
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)


# Task 16: Accept student details and display them using an f-string
name = input("Enter student name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
print(f"My name is {name}. I am {age} years old and my CGPA is {cgpa}.")


# Task 17: Convert Celsius to Fahrenheit and display two decimal places
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")


# Task 18: Check whether an integer is even or odd
number = int(input("Enter number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")
