text = "Hello World! Python Is Fun."

lowercase_count = 0


for char in text:
    if char.islower():  # Check if the character is lowercase
        lowercase_count += 1  # Increase the counter

print("Original string:", text)
print("Number of lowercase letters:", lowercase_count)
