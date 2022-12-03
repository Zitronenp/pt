from sympy import isprime

def prost():
    c = 1
    while True:
        if isprime(c):
            yield c
        c += 1

f=prost()
for i in range(int(input())):
    print(next(f))