# Program to find when the father is twice as old as his son

# collect ages from user

# calculate the difference

# display result

father_age = int(input("Enter father's current age (1 - 80): "))

son_age = int(input("Enter son's current age (1 - 80): "))


years = abs(father_age - (2 * son_age))


print("The father was/will be twice as old as his son in", years, "years.")
