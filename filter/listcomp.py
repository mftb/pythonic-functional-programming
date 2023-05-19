def main():
    return [x*x for x in range(0, 10**8) if (x % 2) == 0]


if __name__ == "__main__":
    result = main()
    print(result[-1])
