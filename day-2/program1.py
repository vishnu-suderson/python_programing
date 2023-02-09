def fibonacci(n):
    if n== 1:
        return 1
    if n== 2:
        return 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter the number of steps in the staircase: "))
print("number of ways to climb the staricase ", fibonacci(n))