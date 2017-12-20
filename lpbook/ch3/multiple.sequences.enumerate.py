# multiple.sequences.enumerate.py
# Reference: w_pacb43.pdf, page 83

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]

print(type(people))
print(enumerate(people))

for position, person in enumerate(people):
    age = ages[position]
    print(person, age)

# EOF
