# Program to find the largest of three numbers

# ask user for three integers

# assume a is the largest

# compare with b

# compare with c

# display result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


largest = a


if b > largest:
    largest = b


if c > largest:
    largest = c


print("The largest number is:", largest)
