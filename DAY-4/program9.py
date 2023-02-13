name = input("Enter your name: ")
height = float(input("Enter your height in meters : "))
weight = float(input("Enter your weight in kg : "))

# Calculate BMI
bmi = weight/(height*height)
print("Hi {}, your BMI is {}".format(name, bmi))

# Determine the BMI category
if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You are normal weight")
else:
    print("You are overweight")
