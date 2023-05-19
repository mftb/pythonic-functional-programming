from functools import reduce


def main():
    return reduce(lambda x, y: x + y, map(lambda x: x*x, range(0, 10**8)), 0)


if __name__ == "__main__":
    result = main()
    print(result)
