# First Non-Repeating Character
# Input: "aabbcdde"out put = c
n = input("enter a string :")
s = ""
for i in n :
    if i.isalpha:
        s += i 
        if s[-1] != i :
            print (i)
            break      


    