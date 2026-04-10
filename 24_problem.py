# 3️⃣ Perfect Number
# Check karo number perfect hai ya nahi.
# Perfect = proper divisors ka sum = number
# Example:
# 6 → 1 + 2 + 3 = 6 ✅
n = int(input("enter a number to check perfect or not :"))
original = n 
sub = 0 
for i in range (1,n):
    if n % i == 0 :
        sub += i 

if sub == original:
    print("this is perfect number :")

else : 
    print("this is not perfect number ")    

