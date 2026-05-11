number = 24

divisor_count = 0  # Start counting from 0

for i in range(1, number + 1):
   
    if number % i == 0:
        divisor_count = divisor_count + 1 


print("Number of divisors of", number, "is", divisor_count)
