x = list(map(int, input().split()))
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
print(multiply(x))