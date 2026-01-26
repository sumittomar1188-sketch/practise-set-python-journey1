'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''
# Taking marks as input
m1 = float(input("Enter marks of Subject 1: "))
m2 = float(input("Enter marks of Subject 2: "))
m3 = float(input("Enter marks of Subject 3: "))

# Calculating total percentage
total_percentage = (m1 + m2 + m3) / 3

# Checking pass/fail condition
if (m1 >= 33 and m2 >= 33 and m3 >= 33) and total_percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

