from functools import reduce


def add(x, y):
    return x + y


def square(x):
    return x*x


def main():
    return reduce(add, map(square, range(0, 10**8)), 0)


if __name__ == "__main__":
    result = main()
    print(result)
