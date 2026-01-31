# Write a program to extract middle digit of a three-digit number.
num = int (input("enter three digit number :"))
middle = (num//10)%10
print (middle)