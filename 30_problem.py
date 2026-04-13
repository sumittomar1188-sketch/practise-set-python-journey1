# 1. Write a program using functions to find greatest of three numbers.
def max (a,b,c):
    if a >b and c :
        print("a is greater :",a)
    elif b>c and a:
        print("b is greater :",b)
    else :
        print("c is greater :",c) 

max (3,41,2)           

# Write a python program using function to convert Celsius to Fahrenhei
def covrt_ferrnite(num):
    if type(num) == int :
        na = (num*9/5) + 32
        print("here converted value of",num,"to ferrinite is -:",na,"'")
    else :
        print("pagal he kya temperature  to dal bhai"  )  

covrt_ferrnite(int(input("enter temperature :")))
     

# How do you prevent a python print() function to print a new line at the end


def inc_convrt(inch):
    cm = inch * 2.54
    print("here the cm value is :-" ,cm,"cm")

(inc_convrt(int(input("enter incher for convert it into cm :"))))    

# table using function 
def table (n):
    for i in range (1,11):
        print(n, "x", i , "=" ,n*i)


table(int(input("enter a number for multiplication table :")))        