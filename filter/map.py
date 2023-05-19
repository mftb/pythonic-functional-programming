def square(x):
    return x*x


def is_even(x):
    return (x % 2) == 0


def main():
    return list(map(square, filter(is_even, range(0, 10**8))))


if __name__ == "__main__":
    result = main()
    print(result[-1])
