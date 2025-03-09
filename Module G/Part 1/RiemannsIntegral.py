from enum import Enum


class RiemannIntegralType(Enum):
    Left = 1
    Right = 2
    Midpoint = 3


def evalulate_integral(f, a: float, b: float, n: int, integralType: RiemannIntegralType):
    step: float = ((b - a) / n)
    total: float = 0.0

    for i in range(n):
        start: float = a + step * i
        end: float = start + step
        mid: float = (start + end) / 2.0

        used_pos = (start if integralType == RiemannIntegralType.Left else (end if integralType == RiemannIntegralType.Right else mid))
        total += step * f(used_pos)

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
        for intType in RiemannIntegralType:
            result: float = evalulate_integral(f, a, b, n, intType)
            print(intType.name, "Riemann Integral Result:", result, "    Accuracy:", result / exact)
        print()