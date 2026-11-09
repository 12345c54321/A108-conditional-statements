#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"


num = int(input("number: "))
if num - round(num) == 0: print("interger")
else print("no interger")