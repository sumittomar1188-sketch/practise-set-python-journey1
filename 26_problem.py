# Number Reverse
# Ek number input lo aur usko reverse karo
# Example: 1234 → 4321
n = int(input("enter a number :"))
s = 0
while n >0 :
    p = n%10
    s =  s*10 +p
    n = n//10

print(s)


