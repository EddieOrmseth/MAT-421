
# bases and numbers must be integers, base_1 and base_m are in decimal, number_1 and number_2 must be written from most significant digit to least significant digit
def convertBaseNToBaseM(base_n: int, number_n: str, base_m: int) -> str:
  decimal: int = 0
  for i in range(0, len(number_n)): # convert number_n from base_n to base_10
    digit: int = int(number_n[len(number_n) - (i + 1)]) # grab the next digit
    decimal += digit * base_n**i # add it with the proper place value

  number_m: str = ""
  while decimal > 0: # convert decimal from base_10 to base_m
    remainder: int = decimal % base_m # grab the remainder
    decimal = int(decimal / base_m) # remove that place value
    number_m = str(remainder) + number_m # add the digit to the base_m number

  return number_m


# test 1
t1_base_n: int = 2 # binary
t1_number_n: str = "11011" # 27
t1_base_m: int = 10 # decimal
t1_number_m: str = "27" # 27

test_t1_number_m: str = convertBaseNToBaseM(t1_base_n, t1_number_n, t1_base_m)
print("Test Number M: " + test_t1_number_m)
print("Test Passed: " + str(t1_number_m == test_t1_number_m))

test_t1_number_n: str = convertBaseNToBaseM(t1_base_m, t1_number_m, t1_base_n)
print("\nTest Number N: " + test_t1_number_n)
print("Test Passed: " + str(t1_number_n == test_t1_number_n))


# test 2
t2_base_n: int = 3 # ternary
t2_number_n: str = "2102" # 65
t2_base_m: int = 8 # octal
t2_number_m: str = "101" # 65

test_t2_number_m: str = convertBaseNToBaseM(t2_base_n, t2_number_n, t2_base_m)
print("\n\nTest Number M: " + test_t2_number_m)
print("Test Passed: " + str(t2_number_m == test_t2_number_m))

test_t2_number_n: str = convertBaseNToBaseM(t2_base_m, t2_number_m, t2_base_n)
print("\nTest Number N: " + test_t2_number_n)
print("Test Passed: " + str(t2_number_n == test_t2_number_n))
