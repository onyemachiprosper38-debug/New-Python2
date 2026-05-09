#ths program asks user to enter their weight
#in (kg) and height in (meters)
# check BMI category

weight = float(input("enter your weight (kg):)

height = float(input("Enter your height (meters):)


bmi = weight / (height * height)

if bmi < 18.5:
    print("Underweight")

elif bmi <= 24.9:
    print("Normal")

elif bmi <= 29.9:
    print("Overweight")

else:
    print("Obese")
