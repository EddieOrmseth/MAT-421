
num_int: int = 12 * 32 * 47 * 39 * 32 * 23 * 234 * 23974 * 2354 * 945 # create a big number
num_float: float = float(num_int) # convert that number to float

print(num_int)
print(num_float)
print("Numbers are equal: " + str(num_float == num_int)) # compare the numbers

print()
num: int = 1
for i in range(0, 50):
    num_int = int(num) # convert to int
    num_float = float(num) # convert to float
    if (num_int != num_float): # if they aren't equal
        print(str(num_int) + " != " + "{:0.10f}".format(num_float)) # print out the numbers
    num *= 10 # check the next one
