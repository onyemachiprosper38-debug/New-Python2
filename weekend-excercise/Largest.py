# Find the largest number in a list
# Find the smallest number in a list
# Count strings where first and last letters are the same

numbers = [10, 20, 5, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)




smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest number is:", smallest)



words = ["abc", "aba", "1221", "xyz", "aa"]

count = 0

for word in words:
    if len(word) >= 2 and word[0] == word[-1]:
        print(word)
        count = count + 1

print("Total matching strings:", count)
