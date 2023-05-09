def square(x):
    return x**2


def main():
    return list(map(square, range(0, 10**7)))


if __name__ == "__main__":
    result = main()
    print(result[-1])
