# Ek number input lo aur check karo Armstrong hai ya nahi.
# Example:
# 153 → 1³ + 5³ + 3³ = 153 ✅

n = int(input("enter a digit to check armstrong or not :"))
original = n 
checking_digit = 0 
for i in str(n):
    checking_digit += int(i)**3


if checking_digit == original:
    print("this number is armstrong")

else :
    print("this number is not armstrong")




