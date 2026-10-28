#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""
num = int(input("enter a number: "))
if num == 0:
    print("your number is 0")
if num > 0:
    print("your number is positive")
if num < 0:
    print("your number is negative")