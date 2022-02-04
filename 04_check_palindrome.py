import pytest


# Solution - two pointers

def is_palindrome(string: str )-> bool:
    if type(string) is not str:
        raise TypeError('input must be a string')

    i = 0
    j = len(string) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    else:
        return True


# Test cases

@pytest.mark.parametrize(
    ('inp', 'result'),
    [
        ('a', True),
        ('racecar', True),
        ('civic', True),
        ('apple', False),
        ('ab', False)
    ]
)
def test_is_palindrome(inp, result):
    assert is_palindrome(inp) == result


def test_is_palindrome_invalid_type():
    with pytest.raises(TypeError):
        assert is_palindrome(123)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
