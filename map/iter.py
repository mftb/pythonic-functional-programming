def main():
    output = list()
    for x in range(0, 10**7):
        output.append(x**2)
    return output


if __name__ == "__main__":
    result = main()
    print(result[-1])
