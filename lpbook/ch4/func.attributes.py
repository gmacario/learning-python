# ch4/func.attributes.py
# Reference: w_pacb43.pdf, page 127

def multiplication(a, b=1):
    """Return a multiped by b. """
    return a * b

special_attributes = [
    "__doc__", "__name__", "__qualname__", "__module__",
    "__defaults__", "__code__", "__globals__", "__dict__",
    "__closure__", "__annotations__", "__kwdefaults__",
]

for attribute in special_attributes:
    print(attribute, '->', getattr(multiplication, attribute))

# EOF
