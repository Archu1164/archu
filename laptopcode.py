# import os
# import platform

# print("System:", platform.system())
# print("Node Name:", platform.node())
# print("Release:", platform.release())
# print("Version:", platform.version())
# print("Machine:", platform.machine())
# print("Processor:", platform.processor())


class Fib:
    def __init__(self, n):
        self.n=n; self.a=0; self.b=1
    def __iter__(self): return self
    def __next__(self):
        if self.n<=0: raise StopIteration
        self.n-=1
        val=self.a
        self.a,self.b=self.b,self.a+self.b
        return val
for x in Fib(5):
    print(x)