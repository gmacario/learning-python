# ch6: decorators/time.measure.start.py
# See w_pacb45.pdf, Page 174

from time import sleep, time

def f():
    sleep(0.3)

def g():
    sleep(0.5)

t = time()
f()
print('f took: ', time() - t)

t = time()
g()
print('g took: ', time() - t)

# EOF
