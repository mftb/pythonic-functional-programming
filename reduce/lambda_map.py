from functools import reduce


def main():
    return reduce(lambda x, y: x + y, list(map(lambda x: x**2, range(0, 10**7))), 0)


if __name__ == "__main__":
    result = main()
    print(result)
