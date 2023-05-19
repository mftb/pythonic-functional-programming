def main():
    output = list()
    for x in range(0, 10**8):
        output.append(x*x)
    return output


if __name__ == "__main__":
    result = main()
    print(result[-1])
