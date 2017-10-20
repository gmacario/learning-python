# scopes1
# Local versus Global
# Reference: w_pacb43.pdf, page 28

def local():
    m = 7
    print(m)

m = 5
print(m)

# we call, or `execute` the function local
local()
