# multiple.sequences.py
# Reference: w_pacb43.pdf, page 81

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]

print(type(people))
print(enumerate(people))

for position in range(len(people)):
    person = people[position]
    age = ages[position]
    print(person, age)

# EOF
