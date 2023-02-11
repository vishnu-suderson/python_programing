n = int(input("enter the number "))
for i in  range(1,(n+1)):
    if i%3 ==0 and i%5==0:
        print("fizzBUZZ")
    elif i%3 ==0 and i%5!=0:
        print("fizz")
    elif i%5==0 and i%3!=0:
        print("buzz")
    else:
        print(i)
