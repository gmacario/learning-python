# ch6: decorators/two.decorators.py
# See w_pacb45.pdf, Page 178

from time import sleep, time
from functools import wraps

def measure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time()
        result = func(*args, **kwargs)
        print(func.__name__, 'took:', time() - t)
        return result
    return wrapper

def max_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result > 100:
            print('{0}: Result is too big ({1}). Max allowed is {2}'
                .format(func.__name__, result, 100))
        return result
    return wrapper

# @measure
@max_result
def cube(n):
    return n ** 3


print(cube(2))
print(cube(5))

# EOF
