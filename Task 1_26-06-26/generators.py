# INSTEAD OF RETURN IT YEILDS THE OUTOUT ONE AT A TIME WITHOUT USING MORE MEMORY

def gen():
    for i in range(16):
        yield i
a = gen()

print(next(a))
print(next(a))

def gen1():
    yield 10
    yield 20
    yield 30

a = gen()

print(next(a))
print(next(a))
print(next(a))

a1 = ( x for x in range(10))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(next(a1))
print(a1)








