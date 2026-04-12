# Number input lo.
# Digits ka sum agar number ko divide kare → Harshad number
# Example: 18 → 1+8=9 → 18 % 9 == 0 ✅


n = int(input("enter a number :"))
original = n 
set = 0 
while n>0 :
    loos = n%10
    set = set + loos
    n = n//10

if original % set == 0:
    print("harshad number :")   

else :
    print("not a harshad number ")


# Number ka square karo, uske digits ka sum agar original number ho → Neon
# Example: 9 → 9²=81 → 8+1=9 ✅    
n = int(input("enter a number :"))
original = n
duplicate = n**2
se = 0 
while duplicate>0 :
    ne = duplicate%10
    se = se + ne
    duplicate = duplicate//10

if se == original :
    print("the number is neon number ")  
else :
    print('the number is not neon ')      



# Spy Number
# Digits ka sum = digits ka product
# Example: 123 → Sum=6, Product=6 ✅
n =  int(input("enter a number :"))
set1 = 0 
set2 = 1
while n>0 :
    pi = n %10
    set1 = set1 + pi 
    set2 = set2 *pi
    n = n//10

if set1 == set2 :
    print("the number is spy nummber :") 

else :
    print("this number is not spy number :")       





# Count Trailing Zeros in Factorial
# Input: 5 → 5! = 120 → Zeros = 1    
n = int(input("enter a number :"))
fact = 1
ser = 0 
for i in range (1,n+1):
    fact = fact*i

fact2 = fact
while fact2 >0 :
    fr = fact2 %10
    if fr== 0 :
        ser += 1
    fact2 = fact2 //10

print("factorial is ",fact,"-","number of zeros are ",ser)         
            
