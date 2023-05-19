def main():
    return list(map(lambda x: x*x, range(0, 10**8)))


if __name__ == "__main__":
    result = main()
    print(result[-1])
