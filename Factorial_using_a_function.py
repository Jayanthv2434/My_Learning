def factorial(n):
    if n<2:
        return 1
    else:
        return n*(factorial(n-1))
sample_number =int(input("Enter a number:"))
result =factorial(sample_number)
print("Factorial of",sample_number,"is:",result)