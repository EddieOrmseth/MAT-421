
one_third: float = 1.0 / 3.0
print("One Third: " + "{:0.20f}".format(one_third))
one: float = one_third * 3.0
print("Result: " + "{:0.20f}".format(one))
print("Is One: " + str(one == 1))


one_small: float = 1.0 / 53982894593057
print("\nOne / Large: " + "{:0.20f}".format(one_third))
one: float = one_small * 53982894593057
print("Result: " + "{:0.20f}".format(one))
print("Is One: " + str(one == 1))


for i in range(200):
    one += one_third
for i in range(200):
    one -= one_third

print("\nResult:" + "{:0.20f}".format(one))
print("Is One: " + str(one == 1))
