import pytest
from soft_assert import SoftAssert

def test_sample_one():
    sa = SoftAssert()

    print("Hai")

    sa.assert_equal(1 + 1, 2, "1+1 should be 2")
    sa.assert_equal(5, 10, "5 should equal 10")
    sa.assert_equal("A", "A", "Strings should match")

    print("works")

    sa.assert_all()


@pytest.mark.xfail(reason="fail skipped")
def test_sample1():
    assert 1 + 1 == 2
    print("welcome")


def test_sample2():
    print("pytest")