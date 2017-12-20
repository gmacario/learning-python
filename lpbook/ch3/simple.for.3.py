# simple.for.3.py
# Reference: w_pacb43.pdf, page 80

surnames = ['Rivest', 'Shamir', 'Adleman']

print(type(surnames))
print(enumerate(surnames))

for position, name in enumerate(surnames):
    print(position, name)

# EOF
