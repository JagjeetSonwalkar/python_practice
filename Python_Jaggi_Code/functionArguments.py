print("----Marvellous Infosystems by Piyush Khairnar----")

print("Demonstration of Types of Function Arguments")

# Position arguments
def Batches1(name,fees):
    print("Batch name is ", name)
    print("Fees are ", fees)
print("Demonstration of Position Arguments")
Batches1('Python', 5000)
Batches1(5000,'Angular')

# Keyword Arguments
def Batches2(name,fees):
    print("Batch name is ", name)
    print("Fees are ", fees)

print("Demonstration Keyword of Arguments")
Batches2(fees=9000, name='PPA')
Batches2(name='LB',fees=7500)

# Default Arguments
def Batches3(name,fees = 5000):
    print("Batch name is ", name)
    print("Fees are ", fees)

print("Demonstration of Default Arguments")

Batches3('Angular',7500)
Batches3('Angular')
Batches3(fees=9000, name='PPA')
Batches3(name='LB')

# Variable number of arguments
def Add(*no):
    ans = 0
    for i in no:
        ans = ans + i
    return ans

print("Demonstration of Variable number of Arguments")

ret = Add(10,20,30)
print("Addition is ", ret)

ret = Add(10,20,30,40,50,60)
print("Addition is ", ret)

ret = Add(10,20)
print("Addition is ", ret)

# Keyword Variable number of arguments

def StudentInfo(**other):
    print(other)
    for i,j in other.items():
        print(i,j)

print("Demonstration of Keyword Variable number of Arguments")

StudentInfo(age=28, address="Sinhagad Road", mobile=7588945488,
company="Marvellous")