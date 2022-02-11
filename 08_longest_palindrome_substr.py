import pytest


# Solution - brute force appraoch
# Check all possible substrings and return longest len palindrome

def solution(string: str) -> int:
    if type(string) is not str:
        raise TypeError('input must be a string')

    # Min length string
    min_window = 1

    # Max length string
    max_window = len(string)

    longest_palindrome = ''
    longest_palindrome_len = 0

    for w in range(min_window, max_window+1):
        for i in range(len(string) - w + 1):
            temp_string = string[i:i+w]

            if temp_string == temp_string[::-1]:
                str_len = len(temp_string)
                if str_len > longest_palindrome_len:
                    longest_palindrome_len = str_len
                    longest_palindrome = temp_string

    return longest_palindrome

# Test cases


@pytest.mark.parametrize(
    ('inp', 'result'),
    [
        ('a', 'a'),
        ('aa', 'aa'),
        ('ccc', 'ccc'),
        ('ab', 'a'),
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('forgeeksskeegfor', 'geeksskeeg'),
        ('abcde', 'a')
    ]
)
def test_solution(inp, result):
    assert solution(inp) == result


def test_solution_invalid_type():
    with pytest.raises(TypeError):
        assert solution(123)


if __name__ == '__main__':
    pytest.main(['-v', '-s', __file__])
