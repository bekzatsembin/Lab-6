x = input()
a = 0
b = 0
for c in x:
    if c.isupper():
        a+=1
    elif c.islower():
        b+=1
print(a, b)