# ch6: decorators/time.measure.dry.py
# See w_pacb45.pdf, Page 174

from time import sleep, time

def f():
    sleep(0.3)

def g():
    sleep(0.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, 'took: ', time() - t)

measure(f);
measure(g);

# EOF
