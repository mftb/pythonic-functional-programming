def main():
    return list(map(lambda x: x**2, range(0, 10**7)))


if __name__ == "__main__":
    result = main()
    print(result[-1])
