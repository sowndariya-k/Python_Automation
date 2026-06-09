import pytest

def test_sample_one():
    print("Hai")
    #pytest.assume(1 + 1 == 3)
    print("works")
    #pytest.assume(5 == 10)
    print("completed")


@pytest.mark.xfail(reason="fail skipped")
def test_sample1():
    assert 1 + 1 == 2
    print("welcome")


def test_sample2():
    print("pytest")

