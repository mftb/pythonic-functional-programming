def generate_list_of_lists():
    return [[x for x in range(0, 3)] for y in range(0, 3)]


def linearize_list_of_lists(list_of_lists):
    return [element for sublist in list_of_lists for element in sublist]


def main():
    list_of_lists = generate_list_of_lists()
    assert len(list_of_lists) == 3
    assert len(linearize_list_of_lists(list_of_lists)) == 9


if __name__ == "__main__":
    main()
