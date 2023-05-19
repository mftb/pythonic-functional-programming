from functools import reduce


def square(x):
    return x*x


def main():
    return sum(list(map(square, range(0, 10**8))))


if __name__ == "__main__":
    result = main()
    print(result)
