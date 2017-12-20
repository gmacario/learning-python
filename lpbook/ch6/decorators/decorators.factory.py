# ch6: decorators/decorators.factory.py
# See w_pacb45.pdf, Page 180

from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print('{0}: Result is too big ({1}). Max allowed is {2}'
                    .format(func.__name__, result, threshold))
            return result
        return wrapper
    return decorator

# @measure
@max_result(75)
def cube(n):
    return n ** 3

print(cube(2))
print(cube(5))

# EOF
