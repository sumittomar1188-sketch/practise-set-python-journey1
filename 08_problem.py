# take input email from user
# input is look like this sumit1234@ gmail.com
# your task is to print sumit1234 

n = input("enter your email :")
pos = n.index("@")
print(n[0:pos])