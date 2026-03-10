# checking palindrome or not
n = input("Enter a string: ").lower()
reverse = n[::-1]

is_palindrome = True

for i in range(len(n)):
    if n[i] != reverse[i]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome hai ✅")
else:
    print("Palindrome nahi hai ❌")


