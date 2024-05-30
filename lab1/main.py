class Tests:
    def Polindrom(self, str):
        for i in range(len(str) // 2):
            if str[i] != str[len(str) - i - 1]:
                return False
        return True

    def Simple(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def Sort(self, array):
        return sorted(array)


def Factorial(n):
    if n < 0:
        raise Exception("Факториал отриц. числа не определен.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def Fibonacci(n):
    if n < 0:
        raise Exception("Число Фибоначчи для отриц. индекса не определено.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n):
        a, b = b, a + b
    return b


def Exponent(a, b):
    return a ** b
