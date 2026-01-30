# Write a program to check whether a three-digit number is palindrome (without if-else, just print result).
num = int (input("enter three digit number "))

first = num//100
middle = (num//10)%10
last = num%10
reverse = last*100 + middle*10 + first
print(reverse==num)

# palindrone means jisme 121 343 999 ese number ho 