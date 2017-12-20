# for.else.py
# Reference: w_pacb43.pdf, page 91

class DriverException(Exception):
    pass

people = [('James', 17), ('Kirk', 9), ('Lars', 13), ('Robert', 8)]

for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    raise DriverException('Driver not found')

print("Driver is", driver)

# EOF
