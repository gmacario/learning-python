# ch6: decorators/time.measure.deco1.py
# See w_pacb45.pdf, Page 175

from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func):
    def wrapper(*args, **kwargs):
        t = time()
        func(*args, **kwargs)
        print(func.__name__, 'took: ', time() - t)
    return wrapper

f = measure(f)      # decoration point

f(0.2)
f(sleep_time=0.3)
print(f.__name__)

# EOF
