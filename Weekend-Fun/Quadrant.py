# Quadrant Finder Program

# ask user for input
# check location
x = int(input("Enter x value: "))
y = int(input("Enter y value: "))


if x > 0 and y > 0:
    print("Q1")

elif x < 0 and y > 0:
    print("Q2")

elif x < 0 and y < 0:
    print("Q3")

elif x > 0 and y < 0:
    print("Q4")

elif x == 0 and y == 0:
    print("Origin")

elif y == 0 and x != 0:
    print("X-axis")

elif x == 0 and y != 0:
    print("Y-axis")
