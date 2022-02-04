import pytest


# Solution - reverse a number and compare

def is_palindrome(num: int )-> bool:
    if type(num) is not int:
        raise TypeError('input must be a integer')
    
    if num < 0:
        return False
    
    rev = 0
    num_copy = num

    while num:
        r = num % 10
        rev = (rev * 10) + r
        num = num // 10

    return num_copy == rev

# Test cases

@pytest.mark.parametrize(
    ('inp', 'result'),
    [
        (1, True),
        (121, True),
        (111, True),
        (123, False),
        (-121, False)
    ]
)
def test_is_palindrome(inp, result):
    assert is_palindrome(inp) == result


def test_is_palindrome_invalid_type():
    with pytest.raises(TypeError):
        assert is_palindrome('aba')


if __name__ == '__main__':
    pytest.main(['-v', '-s', __file__])
