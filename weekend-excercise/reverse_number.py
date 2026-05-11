
number = 12345

number_str = str(number)

reversed_str = ""


for i in range(len(number_str)-1, -1, -1):
    reversed_str += number_str[i]


reversed_number = int(reversed_str)

print("Original number:", number)
print("Reversed number:", reversed_number)
