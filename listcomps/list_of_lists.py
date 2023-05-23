def linearize_list_of_lists(list_of_lists):
    return [element for sublist in list_of_lists for element in sublist]


def main():
    list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert linearize_list_of_lists(list_of_lists) == list(range(1, 10))


if __name__ == "__main__":
    main()
