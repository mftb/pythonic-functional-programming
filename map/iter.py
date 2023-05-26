def main():
    squares = list()
    for x in range(0, 10**8):
        squares.append(x*x)
    return squares


if __name__ == "__main__":
    result = main()
    print(result[-1])
