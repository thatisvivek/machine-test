import pytest

from machine_test.longest_consecutive_subseq import solution_one


@pytest.mark.parametrize(
    ('inp', 'exp'),
    [
        ([1, 9, 3, 10, 4, 20, 2], 4),
        ([36, 41, 56, 35, 44, 33, 34, 92, 43, 32, 42], 5),
        ([1, 3, 5, 7, 9], 1)
    ]
)
def test_lcs_solution_one(inp, exp):
    assert solution_one(inp) == exp
