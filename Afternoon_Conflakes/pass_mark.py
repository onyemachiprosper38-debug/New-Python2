pass_mark = 45

passed = 0
failed = 0


for i in range(1, 16):
    score = int(input(f"Enter score for student {i}: "))

    if score >= pass_mark:
        passed += 1
    else:
        failed += 1

print("\nResults:")
print("Number of students who passed:", passed)
print("Number of students who failed:", failed)
