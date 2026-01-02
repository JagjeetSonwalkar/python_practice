# Input: x=y=z=50
# Output: 50 50 50

# Global variable example
# Input: gx=5, def fun(): print(gx)
# Output: 5

# Local variable example
# Input: x=5, def localFun(): x=10; print(x)
# Output: 10

#  Modify global variable using global
# Input:
# x=5
# def fun():
#  global x
#  x = 20
# fun()
# print(x)
# Output: 20

# Use id() function
# Input: x=100
# Output: (some memory address)

#  Ignore variable using _
# Input: a,b,_ = (1,2,3)
# Output: a=1 b=2

# Assign string with quotes
# Input: msg = "He said 'Hi'"
# Output: He said 'Hi'

# Dynamic typing
# Input: x=10 → x="Ten"
# Output: "Ten"

# Delete variable with del
# Input:
# d=5
# Output: Error: name 'd' is not defined

gx = 5
def fun():
    print(gx)

def localFun():
    x = 10
    print(x)

x = 5
def gloablFun():
    global x
    x = 20
    print(x)

def main():
    a = 50
    x = y = z = a
    print(x,y,z)

    fun()

    localFun()

    gloablFun()

    x = 100
    print(id(x))

    a,b,_ = (1,2,3) # Ignore variable using _
    print("a=",a,"b=",b)

    msg = "He said 'Hi'"
    print(msg)

    a = 10
    numbertoworddict = {10: "ten"}
    numtoWord = numbertoworddict[a]
    print(numtoWord)

    d = 10
    print("d=",d)

    del d
    print(d)

if __name__ == "__main__":
    main()