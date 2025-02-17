from sklearn.linear_model import LinearRegression
import random


def createXDataSet(start: int, end: int) -> list:
    list = []
    for i in range(start, end + 1):
        list.append([i])
    return list


def createYDataSet(x: list) -> list:
    y = []
    for value in x:
        y.append(1 + 2 * value[0] + random.uniform(-.25, .25))
    return y


if __name__ == "__main__":
    model = LinearRegression()

    x = createXDataSet(1, 5)
    y = createYDataSet(x)
    model.fit(x, y)
    print("X Data:", x)
    print("Y Data:", y)
    print("5-pt Intercept:", model.intercept_)
    print("5-pt Slope:", model.coef_)
    print()


    x = createXDataSet(1, 10)
    y = createYDataSet(x)
    model.fit(x, y)
    print("X Data:", x)
    print("Y Data:", y)
    print("10-pt Intercept:", model.intercept_)
    print("10-pt Slope:", model.coef_)
    print()


    x = createXDataSet(1, 20)
    y = createYDataSet(x)
    model.fit(x, y)
    print("X Data:", x)
    print("Y Data:", y)
    print("20-pt Intercept:", model.intercept_)
    print("20-pt Slope:", model.coef_)
    print()


    x = createXDataSet(1, 100)
    y = createYDataSet(x)
    model.fit(x, y)
    print("X Data:", x)
    print("Y Data:", y)
    print("100-pt Intercept:", model.intercept_)
    print("100-pt Slope:", model.coef_)
    print()
