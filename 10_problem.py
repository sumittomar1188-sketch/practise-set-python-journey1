n = input ("enter as string ")
s = ""
l = []
for i in n :
    if i!= " ":
        s = s + i 
    else : 
        l.append(s)
        s = ""

print(l)            


