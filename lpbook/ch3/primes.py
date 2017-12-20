# primes.py
# Reference: w_pacb43.pdf, page 92

primes = []     # This will contain the primes in the end
upto = 100      # The limit, inclusive

for n in range(2, upto + 1):
    is_prime = True     # Flag, new at each iteration of outer for
    for divisor in range(2, n):
        # print("DEBUG: n=", n, ", divisor=", divisor)
        if n % divisor == 0:
            is_prime = False
            break
    if is_prime:    # Check on flag
        primes.append(n)
print(primes)

# EOF
