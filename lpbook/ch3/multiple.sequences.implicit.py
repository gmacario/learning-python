# multiple.sequences.implicit.py
# Reference: w_pacb43.pdf, page 85

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'Bangladesh']

print(type(people))
print(enumerate(people))

for data in zip(people, ages, nationalities):
    # print(data)
    person, age, nationality = data
    print(person, age, nationality)

# EOF
