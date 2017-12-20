# multiple.sequences.zip.py
# Reference: w_pacb43.pdf, page 84

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'Bangladesh']

print(type(people))
print(enumerate(people))

for person, age, nationality in zip(people, ages, nationalities):
    print(person, age, nationality)

# EOF
