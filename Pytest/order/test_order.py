import pytest

@pytest.mark.order(3)
def test_third():
    print("Third Test")

@pytest.mark.order(1)
def test_first():
    print("First Test")

@pytest.mark.order(2)
def test_second():
    print("Second Test")

@pytest.mark.order(4)
def test_fourth():
    print("Fourth Test")