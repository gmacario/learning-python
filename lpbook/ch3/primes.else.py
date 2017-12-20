# primes.else.py
# Reference: w_pacb43.pdf, page 93

primes = []     # This will contain the primes in the end
upto = 100      # The limit, inclusive

for n in range(2, upto + 1):
    for divisor in range(2, n):
        # print("DEBUG: n=", n, ", divisor=", divisor)
        if n % divisor == 0:
            break
    else:
        primes.append(n)
print(primes)

# EOF
