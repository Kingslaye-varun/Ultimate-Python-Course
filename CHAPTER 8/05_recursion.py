#Factorial = n! = n x n-1 x .......x 5 x 4 x 3 x 2 x 1
#Factorial = 5! = 5 x 4 x 3 x 2 x 1
#Factorial = 4! = 4 x 3 x 2 x 1
#Factorial = 3! = 3 x 2 x 1
#Factorial = 2! = 2 x 1
#Factorial = 1! = 1

#Factorial(n) = n * Factorial(n-1)

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return (n * factorial(n - 1))

n = int(input("Enter a No. : "))
print(f"Factorial of {n} is {factorial(n)}")