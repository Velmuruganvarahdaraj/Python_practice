def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def find_primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]
start_range =int(input("Enter the Start_range: "))
end_range = int(input("Enter the End_range: "))
primes = find_primes_in_range(start_range, end_range)
print(f"Prime numbers between {start_range} and {end_range}: {primes}")
