# String Manipulation
# Given a string, count the frequency of each character and return the result as a dictionary.
# Example: "aabcc" → {'a':2, 'b':1, 'c':2}
a = input("enter a string to check ")
num = {}
for i in a :
    if i in num :
        num[i] += 1
    else:
        num[i] = 1
print(num)            

