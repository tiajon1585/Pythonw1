#Ask user to enter their name and student ID
name = input("Enter your name: ")
student_id = input("Enter your Student ID: ")

#Ask the user to enter two different whole numbers
number1 = int(input("Enter a whole number: "))
number2 = int(input("Enter a different second whole number: "))

#Perform three math calculations of my choice
addition = number1 + number2
subtraction = number1 - number2
division = number1 / number2

#Output the results of the three math calculations, showing two decimal places
print(f"The result of {number1} plus {number2} is: {addition:.2f}")
print(f"The result of {number1} minus {number2} is: {subtraction:.2f}")
print(f"The result of {number1} divided by {number2} is: {division:.2f}")

#Determine if the user's first number is larger or smaller than the second number
if number1 > number2:
    print("Number 1 is larger than Number 2")
elif number1 <number2:
      print("Number 1 is smaller than Number 2")
else:
      print("Both numbers are equal")

#Output your users name and studentID
print(name)
print(student_id)
