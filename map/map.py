def square(x):
    return x**2


def main():
    return list(map(square, range(0,100000000)))


if __name__ == "__main__":
    result = main()
    print(result[-1])
