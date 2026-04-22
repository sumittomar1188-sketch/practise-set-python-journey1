# Prime Number Logic

# Write a function to check whether a number is prime or not using optimal approach (not brute force till n).
def prime_number(num):
    try:
        if num % num == 0 and num % 1 == 0 :
            return "prime number"
        else :
            return "not a prime number"
    except:
         return ("bhai integer  dal")    
    
print(prime_number("555"))    