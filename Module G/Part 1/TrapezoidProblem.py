

def evalulate_trap_integral(f, a: float, b: float, n: int):
    step: float = ((b - a) / n)
    total: float = 0.0

    for i in range(n):
        start: float = a + step * i
        end: float = start + step

        total += step * ((f(start) + f(end)) / 2.0)

    return total


if __name__ == '__main__':
    
    f = lambda x: (x-3)**3
    f_int = lambda x: (x-3)**4 * (1.0 / 4.0)

    a = 0
    b = 7
    n_list = [6, 12, 18, 24, 100]

    exact = f_int(b) - f_int(a)

    for n in n_list:
        print("n = ", n)
        result: float = evalulate_trap_integral(f, a, b, n)
        print("Trapzoid Riemann Integral Result:", result, "    Accuracy:", result / exact)
        print()
