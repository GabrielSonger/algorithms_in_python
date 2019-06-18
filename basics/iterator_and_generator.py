
# Simple iterator function implementation
# Any object that implements __next__ can be called iterator

class Fib:
    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur = self.cur + self.prev
            self.prev = value
            self.n -= 1
            return value
        else:
            raise StopIteration()
        
f = Fib(10)
print([i for i in f])

# Generator
def func(n):
    yield n * 2

func
# <function func at 0x00000000029F6EB8>

g = func(5)
g
#<generator object func at 0x0000000002908630>

next(g)
#10

for i in g:
    print(i)
#10

def fib(n):
    prev, curr = 1, 1
    while n > 0:
        n -= 1
        yield prev
        prev, curr = curr, curr + prev

print([i for i in fib(10)])
