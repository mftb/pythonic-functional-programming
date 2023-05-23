def get_volume(abcissa, ordinate, applicate):
    r3 = list()
    for x in range(0, abcissa):
        r2 = list()
        for y in range(0, ordinate):
            r2.append([z for z in range(0, applicate)])
        r3.append(r2)
    return r3


def main():
    cube = get_volume(3, 3, 3)
    linear_cube = [x for z in cube for y in z for x in y]
    assert all([isinstance(x, int) for x in linear_cube])


if __name__ == "__main__":
    main()
