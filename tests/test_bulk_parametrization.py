from classes.tips import total_with_tips
import pytest
@pytest.mark.parametrize(["num1", "num2", "expectation"], [
    (10,20,12),
    (100,20,120),
    (0,0,5)
])
def test_tip_bulk (num1, num2, expectation) :
    assert total_with_tips(num1, num2) == expectation