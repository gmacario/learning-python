# multiple.sequences.zip.py
# Reference: w_pacb43.pdf, page 84

people = ['Jonas', 'Julio', 'Mike', 'Moz']
ages = [25, 30, 31, 39]

print(type(people))
print(enumerate(people))

for person, age in zip(people, ages):
    print(person, age)

# EOF
