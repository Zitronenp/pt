def funcIn(a):
    while True:
        yield a
        a+=1

def func(a):
    while True:
        yield next(funcIn(a))
        a+=1

f=func(2)
for i in range(2):
    print(next(f))