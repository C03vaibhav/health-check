# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Initialize variables for sum, prime count, and composite count
sum_of_numbers = 0
prime_count = 0
composite_count = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):
    sum_of_numbers += num
    if is_prime(num):
        prime_count += 1
    else:
        composite_count += 1

# Print the results
print("Sum of numbers from 1 to 100:", sum_of_numbers)
print("Number of prime numbers in the range:", prime_count)
print("Number of composite numbers in the range:", composite_count)
