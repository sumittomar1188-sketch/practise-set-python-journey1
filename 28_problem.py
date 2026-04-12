# Count Numbers Divisible by 3 and 5 Between 1–100
count = 0
for i in range (1,101):
    if i % 3 == 0   :
        count = count+1
    
    elif i % 5 == 0 :
        count = count+1

print(count)        

# Replace Every Vowel with '*'
n = input("enter string i replace vowels :")
vowel = "AEIOUaeiou"
replacement = ""
for i in n :
    if i.isalpha():
        if i in vowel:
            replacement += "*"
        else :
            replacement += i
            

print(replacement)