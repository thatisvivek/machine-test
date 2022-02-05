import pytest


# Solution - using dict O(2n) complexity

def solution(string: str) -> int:
    if type(string) is not str:
        raise TypeError('input must be a string')

    counter = {}

    for c in string:
        counter[c] = counter.get(c, 0) + 1

    for i, c in enumerate(string):
        if counter[c] == 1:
            return i

    return -1


# Test cases

@pytest.mark.parametrize(
    ('inp', 'result'),
    [
        ('a', 0),
        ('teeterson', 5),
        ('barbar', -1)
    ]
)
def test_solution(inp, result):
    assert solution(inp) == result


def test_solution_invalid_type():
    with pytest.raises(TypeError):
        assert solution(123)


if __name__ == '__main__':
    pytest.main(['-v', '-s', __file__])
