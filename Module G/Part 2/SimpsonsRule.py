

def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n - 1):
        xi = a + h * i

        if i % 2 == 0: # even
            total += 2 * f(xi)
        else: # odd
            total += 4 * f(xi)

    return total * h * (1.0 / 3.0)


if __name__ == '__main__':

    f = lambda x: x ** 2
    F = lambda x: (1.0/3.0) * x ** 3

    real_integral = F(4) - F(0)
    simp_integral_10      = simpsons_rule(f, 0, 4, 10)
    simp_integral_100     = simpsons_rule(f, 0, 4, 100)
    simp_integral_1000    = simpsons_rule(f, 0, 4, 1000)
    simp_integral_10000   = simpsons_rule(f, 0, 4, 10000)
    simp_integral_100000  = simpsons_rule(f, 0, 4, 100000)
    simp_integral_1000000 = simpsons_rule(f, 0, 4, 1000000)


    print("Real Result     :", real_integral, "\n")

    print("N = 10")
    print("Simpson's Result:", simp_integral_10)
    print("Accuracy        :", real_integral / simp_integral_10, "\n")

    print("N = 100")
    print("Simpson's Result:", simp_integral_100)
    print("Accuracy        :", real_integral / simp_integral_100, "\n")

    print("N = 1000")
    print("Simpson's Result:", simp_integral_1000)
    print("Accuracy        :", real_integral / simp_integral_1000, "\n")

    print("N = 10000")
    print("Simpson's Result:", simp_integral_10000)
    print("Accuracy        :", real_integral / simp_integral_10000, "\n")

    print("N = 100000")
    print("Simpson's Result:", simp_integral_100000)
    print("Accuracy        :", real_integral / simp_integral_100000, "\n")

    print("N = 1000000")
    print("Simpson's Result:", simp_integral_1000000)
    print("Accuracy        :", real_integral / simp_integral_1000000, "\n")
