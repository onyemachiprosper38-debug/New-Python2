# Program to calculate average score and grade

# collect three scores

# calculate average

# determine grade

# display result

scoreOne = float(input("Enter first score: "))
scoreTwo= float(input("Enter second score: "))
scoreThree = float(input("Enter third score: "))


average = (scoreOne + scoreTwo + scoreThree) / 3


if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'


print("Average score:", average)
print("Letter grade:", grade)
