##import math
##n = math.log2(1024)
##
##import random
##r = random.random()
##
##import datetime
##d = datetime.datetime.now()
##
##import time
##t1 = time.process_time()
##...

##class Coord:
##    def __init__(self, x, y):
##        self.x = x
##        self.y = y
##
##    def get(self):
##        return (self.x, self.y)
##
##    def add(self, other):
##        return Coord(self.x + other.x, self.y + other.y)
##
##c1 = Coord(1, 1)
##c2 = Coord(2, 3)
##c3 = c1.add(c2)


##with open('spam.txt') as file:
##    for line in file:
##        print(line, end='')
        

##filename = 'spam.txt'
##file = open(filename, 'w')
##file.write('Monty\n')
##file.write('Python\n')
##file.close()


##pairs = [(i,j) for i in range(3)
##               for j in range(3) if i != j]
##print(pairs)


##t = [i*i for i in range(1, 6)]
##print(t)


##s = []
##for i in range(1, 6):
##    s.append(i+i)
##print(s)


##def generator(n):
##    for i in range(n):
##        yield 100 + i
##
##it = generator(4)
##for i in it: print(i)


##def sum_and_diff(a, b):
##    return (a + b, a - b)
##
##x = sum_and_diff(7, 4)
##print(x)


##a = [1, 2, 3]
##a[0]
##print


##a, b, c = 1, 10, 100
##
##def printsum():
##    print(a + b + c)
##
##printsum()


##def add(p, q, r):
##    temp = p + q + r
##    return temp
##
##sum = add(1, 10, 100)
##print(sum)


##for i in range(4):
##    print(i, end=' ')
##
##for i in range(2, 6):
##    print(i, end=' ')
##
##for i in range(0, 8, 2):
##    print(i, end=' ')


##a = 3
##if a == 0:
##    b = 1
##    if c < 0 and d > 0:
##        b = 2
##elif a > 0:
##    b = 3
##else:
##    for i in range(4):
##        b = 4
##        while b > 0:
##            print(b)
##            b = b - 1
##        if i == j: break


## x = a if b < c else d + e


## n = 2
## for i in range(8):
##   n = n * n
##   print(n)

## EOF
