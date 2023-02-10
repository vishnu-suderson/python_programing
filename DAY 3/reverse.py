def reverse(s):
    str = ""
    for i in s:
        str = i +str
    return str

s=input("enter the number")
print("The original string is :",end="")
print(s)

print("The reversed string(using loopd) is : ",end="")
print(reverse(s))