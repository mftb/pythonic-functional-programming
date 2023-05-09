from functools import reduce


def sum(x, y):
    return x + y


def square(x):
    return x**2


def main():
    return reduce(sum, list(map(square, range(0, 10**7))), 0)


if __name__ == "__main__":
    result = main()
    print(result)
