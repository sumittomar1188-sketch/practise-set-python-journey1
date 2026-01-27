# User se ek string lo aur batao:

# kitne vowels

# kitne consonants

n = str(input("enter your name :"))
vowel_count = 0
consunant_count = 0 

vowel = "aeiouAEIOU"
for i in n:
    if i.isalpha():
        if i in vowel:
            vowel_count +=1
        else:
            consunant_count += 1
print("total vowel in given str :",vowel_count)                 
print("total consunants in given str :",consunant_count)
