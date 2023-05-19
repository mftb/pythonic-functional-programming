from functools import reduce


def sum(x, y):
    return x + y


def square(x):
    return x*x


def main():
    return reduce(sum, list(map(square, range(0, 10**8))), 0)


if __name__ == "__main__":
    result = main()
    print(result)
