text = "Hello World! Python Is Fun."

uppercase_count = 0

for char in text:
    if char.isupper(): 
        uppercase_count += 1  

print("Original string:", text)
print("Number of uppercase letters:", uppercase_count)
