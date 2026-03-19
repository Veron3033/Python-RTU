def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


count = int(input("How many prime numbers do you want? "))

primes = []
candidate = 2

while len(primes) < count:
    if is_prime(candidate):
        primes.append(candidate)
    candidate += 1

print(f"First {count} prime numbers:")
print(primes)