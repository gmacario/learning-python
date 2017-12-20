# multiple.sequences.while.py
# Reference: w_pacb43.pdf, page 86

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]
position = 0

print(type(people))
print(enumerate(people))

while position < len(people):
    person = people[position]
    age = ages[position]
    print(person, age)
    position += 1

# EOF
