import sys

import pytest
#def test_sample_one():
#    print("Hai")
#    assert 1+1==3
@pytest.mark.xfail(reason="fail skipped")
def test_sample1():
    print("welcome")
    assert 1+1==2
def test_sample2():
    print("pytest")

#2. assert x==y
@pytest.mark.skipif(sys.version_info<(3,8),reason="this id temporary test")
#def test_equal_assertion():
#    x=5
#    y=6
#    assert x==y
@pytest.mark.skip(reason="this is temporary test")
def test_equal1():
    a=5
    b=5
    assert a==b
@pytest.mark.smoke
def test_equal2():
    a=5
    b=6
    assert a!=b
@pytest.mark.regression
def test_equal3():
    num=[1,2,3,4,5]
    assert 5 in num

@pytest.mark.regression
def test_equal4():
    a="anu"
    b="anu"
    assert a.__eq__(b)

@pytest.mark.parametrize("test_input, expected",[(1,3),(4,6),(5,7)])
def test_add(test_input, expected):
    assert test_input+2==expected
