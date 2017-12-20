# ch6: decorators/time.measure.arguments.py
# See w_pacb45.pdf, Page 175

from time import sleep, time

def f(sleep_time=0.1):
    sleep(sleep_time)

def measure(func, *args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took: ', time() - t)

measure(f, sleep_time=0.3);
measure(f, 0.2);

# EOF
