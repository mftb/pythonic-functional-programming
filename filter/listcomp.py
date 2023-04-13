def main():
    return [x**2 for x in range(0,100000000) if (x % 2) == 0]


if __name__ == "__main__":
    result = main()
    print(result[-1])
