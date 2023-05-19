def main():
    even_squares = list()
    for x in range(0, 10**8):
        if (x % 2) == 0:
            even_squares.append(x*x)
    return even_squares


if __name__ == "__main__":
    result = main()
    print(result[-1])
