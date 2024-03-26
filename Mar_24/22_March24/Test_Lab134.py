import pytest

def test_sub():
    assert 2-2 == 0

def test_add():
    assert 3+3 == 6

@pytest.mark.smoke

def test_sub():
    assert 2+2 == 4
    print("Nitish")

@pytest.mark.skip(reason="Not Implemented Yet")

def test_sub():
    assert 2-1 == 1