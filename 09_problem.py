# count the frequency of the given char in a provided String
# eg- hello how are you , the frequency is 2 
n = input("enter a string :")
s = input("enter frequency which you want to know :")
counter = 0 
for i in n :
    if i == s :
     counter  += 1
print(counter)     

# write a program which can remove particular char from given string
n = input("enter a string :")
s = input("enter frequency which you want to know :") 
# because we can change the existing string so we can made new string using given string 
result = "" # here we made a empty string
for i in n :
   if i != s :
      result = result +i
print(result)      