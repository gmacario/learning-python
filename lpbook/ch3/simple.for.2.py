# simple.for.2.py
# Reference: w_pacb43.pdf, page 80

surnames = ['Rivest', 'Shamir', 'Adleman']

print(type(surnames))

for position in range(len(surnames)):
    print(position, surnames[position])
    # print(surnames[position][0], end='')

# EOF
