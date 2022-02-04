import pytest


# Solution - sort and compare

def is_anagram(string_1: str, string_2: str) -> bool:

    if type(string_1) is not str or type(string_2) is not str:
        raise TypeError('input must be a string')

    if len(string_1) != len(string_2):
        return False

    return sorted(string_1) == sorted(string_2)


# Test cases

@pytest.mark.parametrize(
    ('inp_1', 'inp_2', 'result'),
    [
        ('a', 'a', True),
        ('listen', 'silent', True),
        ('fried', 'fired', True),
        ('gainly', 'laying', True),
        ('abcc', 'abcca', False),
        ('rat', 'car', False),
        ('aad', 'cab', False),
        ('a', 'b', False)
    ]
)
def test_is_anagram(inp_1, inp_2, result):
    assert is_anagram(inp_1, inp_2) == result


def test_is_anagram_invalid_type():
    with pytest.raises(TypeError):
        assert is_anagram(1, 2)


if __name__ == '__main__':
    pytest.main(['-v', __file__])
