import pytest

from {{cookiecutter.package_slug}} import utils


@pytest.mark.parametrize(
    argnames=["int1", "int2", "expected"],
    argvalues=[
        pytest.param(1, 2, 3, id="Positive Numbers"),
        pytest.param(-1, 2, 1, id="Negative Numbers"),
        pytest.param(0, 0, 0, id="0"),
    ],
)
def test_sum(int1: int, int2: int, expected: int):
    assert utils.custom_sum(int1, int2) == expected
    assert utils.custom_sum(int2, int1) == expected
