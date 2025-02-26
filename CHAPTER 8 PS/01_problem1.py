a = 1
b = 2
c = 3

def greatestNumber(a, b, c):
    if(a > b and a > c):
        return a
    elif(b > c and b > a):
        return b
    else:
        return c
    
print(greatestNumber(a, b , c))