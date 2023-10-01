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

nums_sum = 0
primes_num_count = 0
composites_num_count = 0

# Loop through numbers from 1 to 100
for num in range(1, 101):
    nums_sum += num
    if is_prime(num):
        primes_num_count += 1
    else:
        composites_num_count += 1

# Print the results
print("Sum of numbers from 1 to 100:", nums_sum)
print("Number of prime numbers in the range:", primes_num_count)
print("Number of composite numbers in the range:", composites_num_count)
