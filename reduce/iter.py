def main():
    sum_of_squares = 0
    for x in range(0, 10**8):
        sum_of_squares += x*x
    return sum_of_squares


if __name__ == "__main__":
    result = main()
    print(result)
