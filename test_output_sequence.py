from output_sequence import output_sequence


def test_output_sequence():
    assert '0\n01\n012' == output_sequence(2), 'Sequences should match'


if __name__ == "__main__":
    test_output_sequence()
    print("All tests passed!")
