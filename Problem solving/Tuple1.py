# Tuple

# Syntax : ()
# heter
# ordered
# index
# data immutable
# tuple immutable
# duplicate

data = (10, 9.45, "hello", 10, True);

print("Data type is: ",type(data));
print("length is: ",len(data));
print(data);

# data[0] = 11;

# data.append(40);

print("Using for_each: ")
for value in data:
    print(value)

print("using for_loop: ")
for i in range(len(data)):
    print(data[i])