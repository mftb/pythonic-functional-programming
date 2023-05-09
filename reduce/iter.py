def main():
    result = 0
    for x in range(0, 10**7):
        result += x**2
    return result


if __name__ == "__main__":
    result = main()
    print(result)
