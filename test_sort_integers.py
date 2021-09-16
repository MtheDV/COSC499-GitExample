from sort_integers import sort_integers


def test_sort():
    assert [1, 2, 3, 4] == sort_integers([3, 4, 1, 2]), 'Array should be sorted'


if __name__ == "__main__":
    test_sort()
    print("All tests passed!")
