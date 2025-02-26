def sumNaturalNumbers(n):
    if(n == 1):
        return 1
    return sumNaturalNumbers(n-1) + n

n = int(input("Enter the number: "))
print(sumNaturalNumbers(n))