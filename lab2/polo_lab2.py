def factorial(n):
    if n == 1 or n == 0:
        return 1
    if n < 0:
        raise Exception("Отриц. факториал отсутствует")
    else:
        return n * factorial(n - 1)


def cos(x):
    result = 0
    delta = 0
    minDelta = 0.0000001
    n = 0
    delta = pow(-1, n) * pow(x, 2 * n) / factorial(2 * n)
    while abs(delta) > minDelta:
        delta = pow(-1, n) * pow(x, 2 * n) / factorial(2 * n)
        result = result + delta
        n = n + 1

    return result


print(cos(0.5))


def ln(x):
    if x < 0.0:
        raise Exception("ERROR: given negative number (error) in Algorithms::Ln.", 1)
    if x == 0.0:
        return "INFINITY"
    result = 0.0
    delta = 0.0
    minDelta = 0.000000001
    n = 0.0
    a = 2 * n + 1
    delta = 2 * (1.0 / a) * pow((x - 1) / (x + 1), a)
    while abs(delta) > minDelta:
        n = n + 1
        a = 2 * n + 1
        result = result + delta
        delta = 2 * (1.0 / a) * pow((x - 1) / (x + 1), a)

    return result


print(ln(0.1))


def sin(x):
    result = 0
    delta = 0
    minDelta = 0.0000001
    n = 0
    delta = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
    while abs(delta) > minDelta:
        delta = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1)
        result = result + delta
        n = n + 1

    return result


print(sin(0.5))


def func(x):
    result = 0
    if x == 0:
        return "INFINITY"
    if x > 0:
        result = ln(x) * cos(x)
    if x < 0:
        result = abs(sin(x) - cos(x)) / ln(abs(x))
    return result


print(func(0.5))
