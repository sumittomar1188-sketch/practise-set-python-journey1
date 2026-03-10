'''Print numbers from 1 to 50 which are divisible by 5

Take a number from user and print its multiplication table

Count total numbers between 1 to 100

Count even numbers between 1 to 100

Count odd numbers between 1 to 100'''


for i in range(1,51):
    if i%5 == 0:
        print(i)


num = int(input("enter a number: "))
i = 1
while i<11:
    print(num*i)         

    i += 1



i = 1
numbers =0
while i<101:
    i +=1
    numbers +=1

print("total number in 1 to 100 :",numbers)     


count = 0 
for i in range (1,101):
    if i%2==0:
        count += 1
        
print("total number in 1 to 100 :", count)        

i = 1 
count = 0
while i<101:
    i += 2




