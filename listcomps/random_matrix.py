import numpy as np


def get_random_matrix(M, N):
    return np.random.randint(10, size=(M, N))


def main():
    random_matrix = get_random_matrix(4, 4)
    linearized_matrix = [x for line in random_matrix for x in line]
    assert len(linearized_matrix) == 4*4
    assert all([isinstance(x, np.int64) for x in linearized_matrix])
    return linearized_matrix


if __name__ == "__main__":
    print(main())
