from classes.RestaurantReviews import RestaurantReviews, ReviewDoesNotExists
import pytest

def test_remove_valid_review () :
    rr=RestaurantReviews()
    rr.reviews["Cafe Mocha"] = {'comment':"Great coffee and pastries", 'rating':5}
    rr.remove_review('Cafe Mocha')
    assert rr.reviews == {}

def test_remove_invalid_review () :
    with pytest.raises(ReviewDoesNotExists) as e :
        rr=RestaurantReviews()
        rr.remove_review('Cafe Mocha')
    assert str(e.value) == "Cafe Mocha does not have review"