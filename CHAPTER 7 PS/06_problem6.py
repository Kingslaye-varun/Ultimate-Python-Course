# 5! = 5 x 4 x 3 x 2 x 1

n = int(input("Enter a Number : "))

prod = 1

for i in range(1,n + 1):
    prod *= i

print(f"Factorial of {n} is {prod}.")