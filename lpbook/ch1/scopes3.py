# lpbook/ch1/scopes3.py
# Local, Enclosing and Global
# Reference: w_pacb43.pdf, page 29

def enclosing_func():
    m = 13
    def local():
        print(m, 'printing from the local scope')

    # calling the function local
    local()

m = 5
print(m, 'printing from the global scope')

# we call, or `execute` the function local
enclosing_func()
