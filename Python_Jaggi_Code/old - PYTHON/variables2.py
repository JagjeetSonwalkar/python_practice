# Use of is keyword
# Input: a=256, b=256
# Output: True

import copy
import gc
import sys

def main():
    a, b = 256, 256
    print(a is b)
    
    x = None
    print(id(x))

    x = "hi"
    print(id(x))
    x = "hello"
    print(id(x))

    #  Aliasing mutable object
    a = [1,2,3,4]
    b = a
    b.append(5)
    print(a)

    # Shallow copy creates new memory
    x = [1,2]
    y = copy.copy(x)
    print("x=",x,"y=",y) 
    print(x is y)

    # Deep copy
    m = [[1,2],[3,4]]
    n = copy.deepcopy(m)
    m[0][0] = 99
    print(n[0][0])
    print("m=",m,"n=",n)
    print(m in n)

    # Garbage collection manual trigger
    i = gc.collect()
    print("number of objects collected",i)

    # Reference counting
    x = []
    print("Reference counting",sys.getrefcount(x))

    # Forcing string interning
    a = sys.intern("hello world")
    b = sys.intern("hello world")
    print(a is b)


if __name__ == "__main__":
    main()