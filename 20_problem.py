# count the digit given from the user 
n = int(input("enter a number"))
# ye negative value ko positive hi samjhega or loop chalaega
n = abs(n)
count = 0

if n == 0 :
    count = count+1
else :
    while n>0 :
        n = n // 10 # ye last digit remove karke count kar dega 
        count = count+1

print(count)           


