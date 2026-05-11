text = "Hello"


for i in range(len(text)):
    character = text[i]         
    ascii_value = ord(character) 
    print(character, "->", ascii_value)
