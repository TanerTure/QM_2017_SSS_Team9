"""
Testing
"""
import rhf
import pytest 

testdata  = [
    (2, 5, 7),
    (0, 0, 0),
]
@pytest.mark.parametrize("a,b,expected", testdata)
def test_add(a, b, expected):
    assert rhf.add(a, b) == expected
    assert rhf.add(b, a) == expected
                                            
