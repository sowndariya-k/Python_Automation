import pytest
def test_sample_one():
    print("Hai")
    assert 1+1==3
def test_sample1():
    print("welcome")
    assert 1+1==2
def test_sample2():
    print("pytest")

#2. assert x==y
def test_equal_assertion():
    x=5
    y=6
    assert x==y
def test_equal1():
    a=5
    b=5
    assert a==b

def test_equal2():
    a=5
    b=5
    assert a!=b

def test_equal3():
    num=[1,2,3,4,5]
    assert 5 in num
def test_equal4():
    a="anu"
    b="anu"
    assert a.__eq__(b)
