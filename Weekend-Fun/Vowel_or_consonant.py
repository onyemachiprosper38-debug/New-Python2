# Vowel or Consonant Program
# ask user for a letter
# convert to lowercase (to handle A, E, I, O, U also)
# check if input is a single alphabet letter
# check vowel

letter = input("Enter a single letter: ")


letter = letter.lower()


if len(letter) != 1 or not letter.isalpha():
    print("Invalid input")

else:
    
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        print("Vowel")
    else:
        print("Consonant")
