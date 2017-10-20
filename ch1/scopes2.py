# scopes2.py
# Local versus Global
# Reference: w_pacb43.pdf, page 28

def local():
    print(m, 'printing from the local scope')

m = 5
print(m, 'printing from the global scope')

# we call, or `execute` the function local
local()
