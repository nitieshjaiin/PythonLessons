# Fixture (concept in python), pytest
# You can use the fixture to setup, provide, teardown resources in your test cases
# pass some data to other testcases you can use the fixture
import pytest

@pytest.fixture
def sample_data():
    data = [1,2,3,4,5] # type -> list
    return data

@pytest.fixture
def sample_data2():
    return  True

def test_number_sample_data_to_be_injected(sample_data):
    assert len(sample_data) == 5

def test2(sample_data, sample_data2):
    assert 3 in sample_data
    assert sample_data2 is True
