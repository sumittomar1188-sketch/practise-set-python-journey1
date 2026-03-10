# Number input lo.
# Factorial of digits ka sum = number ho to Strong number.
# Example:
# 145 → 1! + 4! + 5! = 145 ✅
n = int(input("enter a number :"))
original = n 
v = 0
for i in str(n):
    i = int(i)
    fact = 1 
    for j in range (1,i+1):
        fact = j*fact
    v += fact

if v == original:
    print("this is equal to originial")
else:
    print("not equal to original")           