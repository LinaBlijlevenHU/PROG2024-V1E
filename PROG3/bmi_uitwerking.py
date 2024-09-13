"""
Write a program that:
• takes as input a person’s height (in meters) and weight (in kilograms)
• computes the person’s BMI and prints ‘underweight’, ‘normal’ or ‘overweight’
Indexes below 18.5 or above 25.0
are assessed as underweight and overweight, respectively; indexes in between are
considered normal
"""

height = float(input("What is your height?"))
weight = float(input("What is your weight?"))

# The Body Mass Index is the value weight / height^2
bmi = weight / height**2

print(f"Your BMI is {bmi:.1f}.")

if bmi > 25.0:
    print("According to your BMI you are overweight.")
elif bmi >= 18.5:
    print("According to your BMI you are a healthy weight.")
else:
    print("According to your BMI you are underweight.")
